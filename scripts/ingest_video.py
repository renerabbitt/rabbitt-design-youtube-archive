"""
Ingest a video transcript into the archive without AI rewriting.

Inbox file format (plain text or markdown):

    Title: Template Tuesdays - Example Title
    URL: https://www.youtube.com/live/VIDEO_ID
    Visibility: members-only

    0:00 Transcript starts here...

Or:

    Template Tuesdays - Example Title
    https://www.youtube.com/live/VIDEO_ID

    0:00 Transcript starts here...

Usage:

    py scripts/ingest_video.py data/inbox/my-video.txt
    py scripts/ingest_video.py --process-inbox
    py scripts/ingest_video.py --title "..." --url "..." --transcript-file path.txt
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
INBOX_DIR = DATA_DIR / "inbox"
PROCESSED_DIR = INBOX_DIR / "processed"
TRANSCRIPTS_DIR = DATA_DIR / "transcripts"
SUMMARIES_DIR = DATA_DIR / "summaries"
VIDEOS_PATH = DATA_DIR / "videos.json"
TAXONOMY_PATH = DATA_DIR / "taxonomy.json"

TIMESTAMP_RE = re.compile(
    r"^(?P<time>(?:\d{1,2}:)?\d{1,2}:\d{2})\s+(?P<text>.+)$"
)
URL_RE = re.compile(
    r"(?:https?://)?(?:www\.)?(?:youtube\.com/(?:watch\?v=|live/|shorts/)|youtu\.be/)([A-Za-z0-9_-]{11})"
)
STOPWORDS = {
    "a",
    "about",
    "all",
    "also",
    "an",
    "and",
    "any",
    "are",
    "as",
    "at",
    "be",
    "because",
    "been",
    "but",
    "by",
    "can",
    "chief",
    "do",
    "for",
    "from",
    "get",
    "going",
    "got",
    "have",
    "here",
    "i",
    "if",
    "in",
    "into",
    "is",
    "it",
    "just",
    "know",
    "like",
    "my",
    "of",
    "on",
    "or",
    "our",
    "out",
    "really",
    "right",
    "so",
    "some",
    "that",
    "the",
    "then",
    "there",
    "these",
    "this",
    "to",
    "um",
    "up",
    "we",
    "what",
    "when",
    "where",
    "with",
    "you",
    "your",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_taxonomy() -> list[dict]:
    return load_json(TAXONOMY_PATH)


def extract_video_id(url: str) -> str:
    match = URL_RE.search(url)
    if not match:
        raise ValueError(f"Could not find a YouTube video ID in URL: {url}")
    return match.group(1)


def normalize_url(url: str, video_id: str) -> str:
    url = url.strip()
    if not url:
        return f"https://www.youtube.com/watch?v={video_id}"
    if url.startswith("http"):
        return url
    return "https://" + url


def timestamp_to_seconds(timestamp: str) -> int:
    parts = [int(part) for part in timestamp.split(":")]
    if len(parts) == 2:
        minutes, seconds = parts
        return minutes * 60 + seconds
    hours, minutes, seconds = parts
    return hours * 3600 + minutes * 60 + seconds


def format_timestamp(seconds: int) -> str:
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def parse_timed_lines(transcript: str) -> list[dict]:
    lines = []
    for raw in transcript.splitlines():
        line = raw.strip()
        if not line:
            continue
        match = TIMESTAMP_RE.match(line)
        if not match:
            continue
        time = match.group("time")
        text = clean_spoken_text(match.group("text"))
        if not text:
            continue
        lines.append({"time": time, "seconds": timestamp_to_seconds(time), "text": text})
    return lines


def clean_spoken_text(text: str) -> str:
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"\s+", " ", text).strip(" -")
    return text


def parse_inbox_payload(text: str) -> dict:
    text = text.lstrip("\ufeff").strip()
    if not text:
        raise ValueError("Empty inbox payload")

    # Strip accidental chat wrappers if pasted whole.
    match = re.search(r"<user_query>\n(?P<body>.*)\n</user_query>", text, flags=re.S)
    if match:
        text = match.group("body").strip()

    lines = [line.lstrip("\ufeff") for line in text.splitlines()]
    meta: dict[str, str] = {}
    body_start = 0

    # Key: value header block
    header_keys = {"title", "url", "visibility", "duration", "durationseconds"}
    first_key = lines[0].split(":", 1)[0].strip().lower() if ":" in lines[0] else ""
    if first_key in header_keys:
        for index, line in enumerate(lines):
            if not line.strip():
                body_start = index + 1
                break
            if ":" not in line:
                body_start = index
                break
            key, value = line.split(":", 1)
            key_norm = key.strip().lower()
            # Stop at transcript timestamps like "0:00 ..." or unknown keys.
            if key_norm not in header_keys:
                body_start = index
                break
            meta[key_norm] = value.strip()
        else:
            body_start = len(lines)
    else:
        # Title / URL / blank / transcript
        if len(lines) < 3:
            raise ValueError("Inbox file needs title, URL, blank line, then transcript")
        meta["title"] = lines[0].strip()
        meta["url"] = lines[1].strip()
        body_start = 2
        if body_start < len(lines) and not lines[body_start].strip():
            body_start += 1

    title = meta.get("title", "").strip()
    url = meta.get("url", "").strip()
    if not title or not url:
        raise ValueError("Title and URL are required")

    transcript = "\n".join(lines[body_start:]).strip()
    # Drop leading non-timestamp chatter if present.
    timed = parse_timed_lines(transcript)
    if timed:
        first = timed[0]["time"] + " "
        pos = transcript.find(first)
        if pos > 0:
            transcript = transcript[pos:].strip()

    if not transcript:
        raise ValueError("Transcript body is empty")

    visibility = meta.get("visibility", "members-only").strip() or "members-only"
    duration_seconds = None
    if meta.get("durationseconds"):
        duration_seconds = int(meta["durationseconds"])
    elif timed:
        duration_seconds = timed[-1]["seconds"]

    return {
        "title": title,
        "url": url,
        "visibility": visibility,
        "durationSeconds": duration_seconds,
        "transcript": transcript,
    }


def classify_text(text: str, taxonomy: list[dict]) -> str:
    normalized = text.lower()
    best_id = "general-overview"
    best_score = 0
    for chapter in taxonomy:
        for subchapter in chapter["subchapters"]:
            hits = [term for term in subchapter["terms"] if term in normalized]
            if not hits:
                continue
            score = sum(len(term) for term in hits) + (len(hits) * 2)
            if score > best_score:
                best_score = score
                best_id = subchapter["id"]
    return best_id


def chapter_title_from_window(texts: list[str]) -> str:
    joined = " ".join(texts)
    # Prefer a sentence-ish chunk.
    candidates = re.split(r"(?<=[\.\!\?])\s+|,\s+(?=[A-Z])", joined)
    for candidate in candidates:
        cleaned = clean_spoken_text(candidate)
        cleaned = re.sub(r"^(um+|uh+|so+|okay+|alright+|and+)\b[\s,]*", "", cleaned, flags=re.I)
        if len(cleaned) >= 28:
            title = cleaned[:110].rstrip(" ,;:")
            if len(cleaned) > 110:
                title += "..."
            return title[0].upper() + title[1:]
    cleaned = clean_spoken_text(joined)[:90].rstrip(" ,;:")
    return (cleaned[0].upper() + cleaned[1:]) if cleaned else "Untitled section"


def build_chapters(timed_lines: list[dict], taxonomy: list[dict], window_seconds: int = 150) -> list[dict]:
    if not timed_lines:
        return []

    chapters = []
    window_start = timed_lines[0]["seconds"]
    window_time = timed_lines[0]["time"]
    bucket: list[str] = []

    def flush(next_line=None):
        nonlocal window_start, window_time, bucket
        if not bucket:
            return
        title = chapter_title_from_window(bucket)
        chapters.append(
            {
                "time": format_timestamp(window_start) if ":" in window_time else window_time,
                "seconds": window_start,
                "title": title,
                "subchapterId": classify_text(title + " " + " ".join(bucket[:8]), taxonomy),
            }
        )
        bucket = []
        if next_line is not None:
            window_start = next_line["seconds"]
            window_time = next_line["time"]

    for line in timed_lines:
        if bucket and line["seconds"] - window_start >= window_seconds:
            flush(line)
        if not bucket:
            window_start = line["seconds"]
            window_time = line["time"]
        bucket.append(line["text"])
    flush()

    # Keep chapter count manageable for long lives.
    if len(chapters) > 45:
        step = max(2, len(chapters) // 35)
        chapters = chapters[::step]
    return chapters


def build_summary_paragraph(title: str, timed_lines: list[dict], topics: list[str]) -> str:
    opening = " ".join(line["text"] for line in timed_lines[:18])
    opening = clean_spoken_text(opening)
    opening = re.sub(r"\s+", " ", opening)
    if len(opening) > 420:
        opening = opening[:417].rstrip(" ,;:") + "..."

    topic_bit = ""
    if topics:
        topic_bit = " Main topics detected: " + ", ".join(topics[:8]) + "."

    return (
        f"Auto-generated draft summary for `{title}`. "
        f"{opening}{topic_bit} "
        "Chapters and keywords were generated from the timed transcript and taxonomy matches. "
        "Optionally polish this draft later; it is already searchable."
    )


def detect_topics_and_keywords(transcript: str, taxonomy: list[dict]) -> tuple[list[str], list[str]]:
    lowered = transcript.lower()
    scored: list[tuple[int, str, list[str]]] = []
    for chapter in taxonomy:
        for subchapter in chapter["subchapters"]:
            hits = [term for term in subchapter["terms"] if term in lowered]
            if hits:
                # Prefer stronger matches: more hits and longer/more specific terms.
                score = sum(len(term) for term in hits) + (len(hits) * 2)
                scored.append((score, subchapter["title"], hits))

    scored.sort(key=lambda item: (-item[0], item[1]))

    topics = []
    keywords = []
    for _score, title, hits in scored:
        topics.append(title)
        keywords.extend(hits[:3])
        keywords.append(title)

    # Lightweight title-ish phrases from frequent content words.
    words = re.findall(r"[a-zA-Z][a-zA-Z\-]{3,}", lowered)
    counts = Counter(word for word in words if word not in STOPWORDS)
    for word, _ in counts.most_common(12):
        if word not in {k.lower() for k in keywords}:
            keywords.append(word)

    # Deduplicate while preserving order.
    topics = list(dict.fromkeys(topics))
    keywords = list(dict.fromkeys(keywords))
    return topics[:16], keywords[:28]


def write_transcript_file(video_id: str, title: str, url: str, transcript: str) -> Path:
    path = TRANSCRIPTS_DIR / f"{video_id}.md"
    content = (
        f"---\n"
        f"videoId: {video_id}\n"
        f"title: {title}\n"
        f'url: "{url}"\n'
        f"status: imported\n"
        f"---\n\n"
        f"# Transcript\n\n"
        f"{transcript.strip()}\n"
    )
    path.write_text(content, encoding="utf-8")
    return path


def write_summary_file(
    video_id: str,
    title: str,
    url: str,
    summary: str,
    topics: list[str],
    chapters: list[dict],
    keywords: list[str],
) -> Path:
    path = SUMMARIES_DIR / f"{video_id}.md"
    chapter_lines = "\n".join(f"- `{chapter['time']}` {chapter['title']}" for chapter in chapters)
    topic_lines = "\n".join(f"- {topic}" for topic in topics) or "- General"
    keyword_lines = "\n".join(f"- {keyword}" for keyword in keywords) or f"- {title}"
    content = (
        f"---\n"
        f"videoId: {video_id}\n"
        f"title: {title}\n"
        f'url: "{url}"\n'
        f"generatedAt: {datetime.now(timezone.utc).isoformat()}\n"
        f"generator: scripts/ingest_video.py\n"
        f"---\n\n"
        f"# Summary\n\n"
        f"{summary}\n\n"
        f"## Key Topics\n\n"
        f"{topic_lines}\n\n"
        f"## Chapters\n\n"
        f"{chapter_lines}\n\n"
        f"## Search Keywords\n\n"
        f"{keyword_lines}\n"
    )
    path.write_text(content, encoding="utf-8")
    return path


def upsert_catalog_entry(entry: dict) -> None:
    catalog = load_json(VIDEOS_PATH)
    videos = catalog.get("videos", [])
    existing = next((video for video in videos if video.get("id") == entry["id"]), None)
    if existing:
        existing.update(entry)
    else:
        # Keep ready/imported content near the top, after any already-ready items.
        insert_at = 0
        for index, video in enumerate(videos):
            if video.get("status") != "ready":
                insert_at = index
                break
            insert_at = index + 1
        videos.insert(insert_at, entry)
    catalog["videos"] = videos
    write_json(VIDEOS_PATH, catalog)


def rebuild_site() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_site_data.py")],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr or result.stdout or "build_site_data.py failed")
    print(result.stdout.strip())


def ingest_payload(payload: dict, rebuild: bool = True) -> dict:
    taxonomy = load_taxonomy()
    video_id = extract_video_id(payload["url"])
    url = normalize_url(payload["url"], video_id)
    title = payload["title"].strip()
    transcript = payload["transcript"].strip()
    timed_lines = parse_timed_lines(transcript)
    chapters = build_chapters(timed_lines, taxonomy)
    topics, keywords = detect_topics_and_keywords(transcript, taxonomy)
    summary = build_summary_paragraph(title, timed_lines, topics)

    transcript_path = write_transcript_file(video_id, title, url, transcript)
    summary_path = write_summary_file(video_id, title, url, summary, topics, chapters, keywords)

    duration_seconds = payload.get("durationSeconds")
    if duration_seconds is None and timed_lines:
        duration_seconds = timed_lines[-1]["seconds"]

    entry = {
        "id": video_id,
        "title": title,
        "url": url,
        "publishedAt": "",
        "durationSeconds": duration_seconds,
        "description": summary.split(". ", 1)[0] + ".",
        "tags": keywords[:10],
        "topics": topics[:10],
        "viewCount": None,
        "thumbnail": "",
        "transcriptPath": f"data/transcripts/{video_id}.md",
        "summaryPath": f"data/summaries/{video_id}.md",
        "status": "ready",
        "visibility": payload.get("visibility", "members-only"),
    }
    upsert_catalog_entry(entry)

    if rebuild:
        rebuild_site()

    return {
        "id": video_id,
        "title": title,
        "transcriptPath": str(transcript_path.relative_to(ROOT)),
        "summaryPath": str(summary_path.relative_to(ROOT)),
        "chapters": len(chapters),
        "topics": len(topics),
        "keywords": len(keywords),
    }


def process_inbox_file(path: Path, rebuild: bool = True) -> dict:
    payload = parse_inbox_payload(path.read_text(encoding="utf-8"))
    result = ingest_payload(payload, rebuild=rebuild)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    target = PROCESSED_DIR / f"{stamp}-{path.name}"
    shutil.move(str(path), str(target))
    result["processedTo"] = str(target.relative_to(ROOT))
    return result


def process_inbox(rebuild_once: bool = True) -> list[dict]:
    skip_names = {"readme.md", "readme.txt", "example.txt", "example.md"}
    files = sorted(
        [
            path
            for path in INBOX_DIR.iterdir()
            if path.is_file()
            and path.suffix.lower() in {".txt", ".md"}
            and path.name.lower() not in skip_names
            and not path.name.lower().startswith("example.")
        ]
    )
    if not files:
        print("No inbox files found in data/inbox/")
        return []

    results = []
    for index, path in enumerate(files):
        rebuild = rebuild_once and index == len(files) - 1
        print(f"Ingesting {path.name}...")
        result = process_inbox_file(path, rebuild=rebuild)
        results.append(result)
        print(
            f"  -> {result['id']}: {result['chapters']} chapters, "
            f"{result['topics']} topics, {result['keywords']} keywords"
        )
    if results and not rebuild_once:
        rebuild_site()
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest YouTube transcripts into the searchable archive.")
    parser.add_argument("inbox_file", nargs="?", help="Path to an inbox file with title/url/transcript")
    parser.add_argument("--process-inbox", action="store_true", help="Process all files in data/inbox/")
    parser.add_argument("--title")
    parser.add_argument("--url")
    parser.add_argument("--transcript-file")
    parser.add_argument("--visibility", default="members-only")
    parser.add_argument("--no-rebuild", action="store_true")
    args = parser.parse_args()

    rebuild = not args.no_rebuild

    if args.process_inbox:
        process_inbox(rebuild_once=rebuild)
        return

    if args.inbox_file:
        result = process_inbox_file(Path(args.inbox_file), rebuild=rebuild)
        print(json.dumps(result, indent=2))
        return

    if args.title and args.url and args.transcript_file:
        transcript = Path(args.transcript_file).read_text(encoding="utf-8")
        payload = {
            "title": args.title,
            "url": args.url,
            "visibility": args.visibility,
            "transcript": transcript,
            "durationSeconds": None,
        }
        # If transcript file already includes headers, prefer parser.
        if transcript.lstrip().lower().startswith("title:") or URL_RE.search(
            "\n".join(transcript.splitlines()[:3])
        ):
            payload = parse_inbox_payload(transcript)
            payload["visibility"] = args.visibility or payload.get("visibility", "members-only")
        result = ingest_payload(payload, rebuild=rebuild)
        print(json.dumps(result, indent=2))
        return

    parser.error("Provide an inbox file, --process-inbox, or --title/--url/--transcript-file")


if __name__ == "__main__":
    main()
