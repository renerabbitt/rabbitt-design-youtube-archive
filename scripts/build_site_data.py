import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SITE_DIR = ROOT / "site"


def load_taxonomy() -> list:
    return json.loads((DATA_DIR / "taxonomy.json").read_text(encoding="utf-8"))


def load_playlists() -> list[dict]:
    path = DATA_DIR / "playlists.json"
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("playlists") or []


TAXONOMY = load_taxonomy()


def split_frontmatter(markdown: str) -> tuple[dict, str]:
    if not markdown.startswith("---\n"):
        return {}, markdown

    _, frontmatter, body = markdown.split("---", 2)
    meta = {}
    for line in frontmatter.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, body.strip()


def section(markdown: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)"
    match = re.search(pattern, markdown, flags=re.M | re.S)
    return match.group("body").strip() if match else ""


def bullet_items(text: str) -> list[str]:
    return [line[2:].strip() for line in text.splitlines() if line.startswith("- ")]


def parse_chapters(text: str) -> list[dict]:
    chapters = []
    for item in bullet_items(text):
        match = re.match(r"`(?P<time>[^`]+)`\s+(?P<title>.+)", item)
        if not match:
            continue
        timestamp = match.group("time")
        chapters.append(
            {
                "time": timestamp,
                "seconds": timestamp_to_seconds(timestamp),
                "title": match.group("title"),
                "subchapterId": classify_text(match.group("title")),
            }
        )
    return chapters


def timestamp_to_seconds(timestamp: str) -> int:
    parts = [int(part) for part in timestamp.split(":")]
    if len(parts) == 2:
        minutes, seconds = parts
        return minutes * 60 + seconds
    if len(parts) == 3:
        hours, minutes, seconds = parts
        return hours * 3600 + minutes * 60 + seconds
    return 0


def classify_text(text: str) -> str:
    normalized = text.lower()
    best_subchapter = "general-overview"
    best_score = 0

    for chapter in TAXONOMY:
        for subchapter in chapter["subchapters"]:
            score = sum(1 for term in subchapter["terms"] if term in normalized)
            if score > best_score:
                best_score = score
                best_subchapter = subchapter["id"]

    return best_subchapter


def youtube_embed_url(url: str, video_id: str) -> str:
    if not video_id:
        return ""
    return f"https://www.youtube.com/embed/{video_id}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def build_index() -> dict:
    catalog = json.loads((DATA_DIR / "videos.json").read_text(encoding="utf-8"))
    ready_videos = catalog["videos"]
    playlist_membership: dict[str, list[str]] = {}
    for playlist in load_playlists():
        playlist_id = playlist.get("id")
        if not playlist_id:
            continue
        for video_id in playlist.get("videoIds") or []:
            playlist_membership.setdefault(video_id, []).append(playlist_id)

    videos = []
    taxonomy = json.loads(json.dumps(TAXONOMY))
    ready_ids = {video["id"] for video in ready_videos}

    for video in ready_videos:
        summary_path = ROOT / video.get("summaryPath", "")
        transcript_path = ROOT / video.get("transcriptPath", "")
        summary_meta, summary_body = split_frontmatter(read_text(summary_path))
        _, transcript_body = split_frontmatter(read_text(transcript_path))

        summary_text = summary_body.split("## Key Topics", 1)[0].strip()
        key_topics = bullet_items(section(summary_body, "Key Topics"))
        keywords = bullet_items(section(summary_body, "Search Keywords"))
        chapters = parse_chapters(section(summary_body, "Chapters"))

        subchapter_ids = sorted({chapter["subchapterId"] for chapter in chapters})
        for chapter in taxonomy:
            for subchapter in chapter["subchapters"]:
                if subchapter["id"] in subchapter_ids:
                    subchapter.setdefault("videoIds", []).append(video["id"])

        playlist_ids = playlist_membership.get(video["id"], [])
        videos.append(
            {
                "id": video["id"],
                "title": video.get("title") or summary_meta.get("title") or "",
                "url": video.get("url") or summary_meta.get("url") or "",
                "embedUrl": youtube_embed_url(video.get("url", ""), video["id"]),
                "visibility": video.get("visibility", "public"),
                "durationSeconds": video.get("durationSeconds"),
                "description": video.get("description", ""),
                "summary": summary_text,
                "topics": key_topics or video.get("topics", []),
                "keywords": keywords or video.get("tags", []),
                "chapters": chapters,
                "playlistIds": playlist_ids,
                "transcript": transcript_body,
                "transcriptAvailable": bool(transcript_body.strip()),
                "searchText": " ".join(
                    [
                        video.get("title", ""),
                        video.get("description", ""),
                        summary_text,
                        " ".join(key_topics),
                        " ".join(keywords),
                        " ".join(chapter["title"] for chapter in chapters),
                        transcript_body,
                    ]
                ).lower(),
            }
        )

    playlists = []
    for playlist in load_playlists():
        playlist_id = playlist.get("id")
        if not playlist_id:
            continue
        video_ids = [video_id for video_id in (playlist.get("videoIds") or []) if video_id in ready_ids]
        # Prefer indexed membership order from the playlist itself; fall back to all listed IDs.
        all_ids = list(playlist.get("videoIds") or [])
        playlists.append(
            {
                "id": playlist_id,
                "title": playlist.get("title") or "",
                "url": playlist.get("url") or "",
                "description": playlist.get("description") or "",
                "thumbnail": playlist.get("thumbnail") or "",
                "videoIds": all_ids,
                "videoCount": playlist.get("videoCount") or len(all_ids),
                "indexedVideoIds": video_ids,
                "indexedCount": len(video_ids),
            }
        )

    return {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "channel": catalog["channel"],
        "stats": {
            "totalVideos": len(catalog["videos"]),
            "readyVideos": len(videos),
            "transcriptVideos": sum(v["transcriptAvailable"] for v in videos),
            "playlistCount": len(playlists),
        },
        "taxonomy": taxonomy,
        "playlists": playlists,
        "videos": videos,
    }


def main() -> None:
    SITE_DIR.mkdir(exist_ok=True)
    index = build_index()
    out_path = SITE_DIR / "search-index.json"
    out_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(index['videos'])} searchable videos to {out_path}")


if __name__ == "__main__":
    main()
