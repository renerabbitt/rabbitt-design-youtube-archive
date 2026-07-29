"""
Fetch YouTube captions into data/inbox/ and optionally ingest them.

Primary path (skips Merlin for most videos):

    py scripts/fetch_transcripts.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
    py scripts/fetch_transcripts.py --pending --limit 10

Members-only / VIP videos usually need browser cookies while you are logged in:

    py scripts/fetch_transcripts.py --url "..." --browser chrome

If captions are unavailable, use scripts/clipboard_to_inbox.py with a Merlin paste.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
INBOX_DIR = DATA_DIR / "inbox"
VIDEOS_PATH = DATA_DIR / "videos.json"

URL_RE = re.compile(
    r"(?:https?://)?(?:www\.)?(?:youtube\.com/(?:watch\?v=|live/|shorts/)|youtu\.be/)([A-Za-z0-9_-]{11})"
)
TAG_RE = re.compile(r"<[^>]+>")
TIMESTAMP_CUE_RE = re.compile(
    r"(?P<start>\d{2}:\d{2}:\d{2}\.\d{3})\s+-->\s+(?P<end>\d{2}:\d{2}:\d{2}\.\d{3})"
)


def extract_video_id(value: str) -> str:
    match = URL_RE.search(value.strip())
    if match:
        return match.group(1)
    value = value.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", value):
        return value
    raise ValueError(f"Could not find a YouTube video id in: {value}")


def normalize_url(video_id: str, live: bool = False) -> str:
    if live:
        return f"https://www.youtube.com/live/{video_id}"
    return f"https://www.youtube.com/watch?v={video_id}"


def load_catalog() -> dict:
    return json.loads(VIDEOS_PATH.read_text(encoding="utf-8"))


def find_catalog_video(video_id: str) -> dict | None:
    catalog = load_catalog()
    return next((video for video in catalog.get("videos", []) if video.get("id") == video_id), None)


def pending_videos(force: bool = False, public_only: bool = False) -> list[dict]:
    videos = load_catalog().get("videos", [])
    pending = []
    for video in videos:
        status = video.get("status", "needs-transcript")
        if status in {"needs-manual-transcript", "no-captions"} and not force:
            continue
        transcript_path = ROOT / video.get("transcriptPath", f"data/transcripts/{video['id']}.md")
        has_transcript = transcript_path.exists() and transcript_path.stat().st_size > 80
        visibility = (video.get("visibility") or "").lower()
        if public_only and visibility in {"members-only", "member", "vip"}:
            continue
        if force or status != "ready" or not has_transcript:
            pending.append(video)
    return pending


def mark_catalog_visibility(video_id: str, visibility: str) -> None:
    catalog = load_catalog()
    changed = False
    for video in catalog.get("videos", []):
        if video.get("id") == video_id:
            if video.get("visibility") != visibility:
                video["visibility"] = visibility
                changed = True
            break
    if changed:
        VIDEOS_PATH.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")


def is_members_only_error(message: str) -> bool:
    lowered = message.lower()
    return any(
        needle in lowered
        for needle in (
            "members-only",
            "members on level",
            "join this channel to get access",
            "member-only",
        )
    )


def format_timestamp(seconds: float) -> str:
    total = max(0, int(seconds))
    hours, rem = divmod(total, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def parse_vtt_timestamp(value: str) -> float:
    hours, minutes, rest = value.split(":")
    seconds, millis = rest.split(".")
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(millis) / 1000


def clean_vtt_text(text: str) -> str:
    text = TAG_RE.sub("", text)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    return re.sub(r"\s+", " ", text).strip()


def vtt_to_timed_transcript(vtt_text: str) -> str:
    """Convert YouTube VTT (including auto-captions) into Merlin-style timed lines."""
    lines: list[tuple[float, str]] = []
    blocks = re.split(r"\n\s*\n", vtt_text.strip())
    for block in blocks:
        block_lines = [line.strip("\ufeff") for line in block.splitlines() if line.strip()]
        if not block_lines:
            continue
        cue_index = next((i for i, line in enumerate(block_lines) if TIMESTAMP_CUE_RE.search(line)), None)
        if cue_index is None:
            continue
        match = TIMESTAMP_CUE_RE.search(block_lines[cue_index])
        if not match:
            continue
        start = parse_vtt_timestamp(match.group("start"))
        text_lines = block_lines[cue_index + 1 :]
        # Prefer the clean full-line cue YouTube duplicates without word-level tags.
        candidates = [clean_vtt_text(line) for line in text_lines]
        candidates = [line for line in candidates if line]
        if not candidates:
            continue
        text = max(candidates, key=len)
        if not text:
            continue
        if lines and lines[-1][1] == text:
            continue
        lines.append((start, text))

    return "\n".join(f"{format_timestamp(start)} {text}" for start, text in lines)


def run_yt_dlp(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "yt_dlp", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


DEFAULT_COOKIES_PATH = DATA_DIR / "youtube.cookies.txt"


def resolve_auth_args(browser: str | None, cookies_file: Path | None) -> list[str]:
    """Prefer an explicit cookies.txt file; otherwise fall back to browser cookies."""
    if cookies_file is not None:
        if not cookies_file.exists():
            raise FileNotFoundError(
                f"Cookies file not found: {cookies_file}\n"
                "Follow docs/cookies-setup.md and export youtube.cookies.txt first."
            )
        return ["--cookies", str(cookies_file)]
    if browser:
        return ["--cookies-from-browser", browser]
    return []


def fetch_metadata(url: str, auth_args: list[str]) -> dict:
    args = ["--skip-download", "--dump-single-json", "--no-warnings", *auth_args, url]
    result = run_yt_dlp(args)
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout or "yt-dlp metadata failed").strip())
    return json.loads(result.stdout)


def choose_subtitle_file(temp_dir: Path, video_id: str) -> Path:
    candidates = sorted(temp_dir.glob(f"{video_id}.*.vtt"))
    if not candidates:
        raise FileNotFoundError(f"No VTT subtitle files downloaded for {video_id}")

    def rank(path: Path) -> tuple[int, str]:
        name = path.name.lower()
        score = 0
        if ".en-orig." in name:
            score += 30
        if ".en." in name or name.endswith(".en.vtt"):
            score += 20
        if "en" in name:
            score += 10
        # Prefer non-auto if both exist with same lang naming; yt-dlp names don't always distinguish.
        return (-score, name)

    return sorted(candidates, key=rank)[0]


def download_subtitles(url: str, video_id: str, auth_args: list[str], temp_dir: Path) -> Path:
    outtmpl = str(temp_dir / "%(id)s.%(ext)s")
    args = [
        "--skip-download",
        "--write-sub",
        "--write-auto-sub",
        "--sub-langs",
        "en.*,en",
        "--sub-format",
        "vtt/best",
        "--no-warnings",
        "-o",
        outtmpl,
        *auth_args,
        url,
    ]
    result = run_yt_dlp(args)
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout or "yt-dlp subtitle download failed").strip())
    return choose_subtitle_file(temp_dir, video_id)


def infer_visibility(meta: dict, catalog_video: dict | None) -> str:
    if catalog_video and catalog_video.get("visibility"):
        return catalog_video["visibility"]
    availability = (meta.get("availability") or "").lower()
    if "member" in availability or meta.get("is_members_only"):
        return "members-only"
    return "public"


def write_inbox_file(
    video_id: str,
    title: str,
    url: str,
    visibility: str,
    transcript: str,
) -> Path:
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    path = INBOX_DIR / f"{video_id}.txt"
    content = (
        f"Title: {title}\n"
        f"URL: {url}\n"
        f"Visibility: {visibility}\n"
        f"\n"
        f"{transcript.strip()}\n"
    )
    path.write_text(content, encoding="utf-8")
    return path


def fetch_one(
    url_or_id: str,
    auth_args: list[str],
    visibility_override: str | None = None,
    title_override: str | None = None,
    force: bool = False,
) -> dict:
    video_id = extract_video_id(url_or_id)
    catalog_video = find_catalog_video(video_id)
    if catalog_video and catalog_video.get("status") == "ready" and not force:
        return {
            "id": video_id,
            "skipped": True,
            "reason": "already ready (pass --force to refetch)",
        }

    preferred_url = (
        catalog_video.get("url")
        if catalog_video and catalog_video.get("url")
        else normalize_url(video_id, live="live/" in url_or_id)
    )
    if not preferred_url.startswith("http"):
        preferred_url = normalize_url(video_id)

    meta = None
    last_error = None
    auth_attempts = [auth_args]
    # If cookies/browser auth fails on public content, retry anonymously once.
    if auth_args:
        auth_attempts.append([])

    with tempfile.TemporaryDirectory(prefix="yt-subs-") as tmp:
        temp_dir = Path(tmp)
        vtt_path = None
        for attempt_auth in auth_attempts:
            try:
                meta = fetch_metadata(preferred_url, attempt_auth)
                vtt_path = download_subtitles(preferred_url, video_id, attempt_auth, temp_dir)
                break
            except Exception as exc:  # noqa: BLE001 - collect and try next strategy
                last_error = exc
                continue
        if vtt_path is None or meta is None:
            raise RuntimeError(
                f"Could not fetch captions for {video_id}. "
                f"Export data/youtube.cookies.txt (see docs/cookies-setup.md), "
                f"or use scripts/clipboard_to_inbox.py with a Merlin paste. "
                f"Last error: {last_error}"
            )

        transcript = vtt_to_timed_transcript(vtt_path.read_text(encoding="utf-8"))
        if len(transcript.splitlines()) < 3:
            raise RuntimeError(
                f"Caption file for {video_id} was empty or too short after parsing. "
                "Use scripts/clipboard_to_inbox.py with a Merlin paste."
            )

        title = title_override or meta.get("title") or (catalog_video or {}).get("title") or video_id
        visibility = visibility_override or infer_visibility(meta, catalog_video)
        watch_url = meta.get("webpage_url") or preferred_url
        inbox_path = write_inbox_file(video_id, title, watch_url, visibility, transcript)

    return {
        "id": video_id,
        "title": title,
        "visibility": visibility,
        "inboxPath": str(inbox_path.relative_to(ROOT)),
        "lines": len(transcript.splitlines()),
        "skipped": False,
    }


def run_ingest(rebuild: bool = True) -> None:
    cmd = [sys.executable, str(ROOT / "scripts" / "ingest_video.py"), "--process-inbox"]
    if not rebuild:
        cmd.append("--no-rebuild")
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.returncode != 0:
        raise RuntimeError(result.stderr or result.stdout or "ingest_video.py failed")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch YouTube captions into the archive inbox.")
    parser.add_argument("--url", help="YouTube URL or video id")
    parser.add_argument("--pending", action="store_true", help="Fetch videos marked needs-transcript")
    parser.add_argument("--limit", type=int, default=5, help="Max pending videos to fetch")
    parser.add_argument(
        "--public-only",
        action="store_true",
        help="Skip catalog videos already marked members-only",
    )
    parser.add_argument(
        "--members-only",
        action="store_true",
        help="Only fetch catalog videos marked members-only",
    )
    parser.add_argument(
        "--cookies",
        help="Path to Netscape cookies.txt (default: data/youtube.cookies.txt if present)",
    )
    parser.add_argument(
        "--browser",
        default="chrome",
        help="Browser for cookies if no cookies file (chrome/edge/firefox/none)",
    )
    parser.add_argument("--visibility", help="Override visibility (public/members-only)")
    parser.add_argument("--title", help="Override title")
    parser.add_argument("--force", action="store_true", help="Refetch even if status is ready")
    parser.add_argument("--no-ingest", action="store_true", help="Only write inbox files")
    parser.add_argument("--no-rebuild", action="store_true", help="Ingest without rebuilding search index")
    args = parser.parse_args()

    if not args.url and not args.pending:
        parser.error("Provide --url and/or --pending")
    if args.public_only and args.members_only:
        parser.error("Use only one of --public-only or --members-only")

    cookies_file = None
    if args.cookies:
        cookies_file = Path(args.cookies)
        if not cookies_file.is_absolute():
            cookies_file = ROOT / cookies_file
    elif DEFAULT_COOKIES_PATH.exists():
        cookies_file = DEFAULT_COOKIES_PATH

    browser = None if args.browser.lower() in {"none", "off", "false", "0"} else args.browser
    if cookies_file is not None:
        browser = None
    auth_args = resolve_auth_args(browser, cookies_file)
    if cookies_file is not None:
        print(f"Using cookies file: {cookies_file}")

    targets: list[str] = []
    if args.url:
        targets.append(args.url)
    if args.pending:
        pending = pending_videos(force=args.force, public_only=args.public_only)
        if args.members_only:
            pending = [
                video
                for video in pending
                if (video.get("visibility") or "").lower() in {"members-only", "member", "vip"}
            ]
        for video in pending[: args.limit]:
            targets.append(video.get("url") or video["id"])

    # De-dupe while preserving order.
    seen = set()
    unique_targets = []
    for target in targets:
        video_id = extract_video_id(target)
        if video_id in seen:
            continue
        seen.add(video_id)
        unique_targets.append(target)

    results = []
    failures = []
    wrote_any = False
    for target in unique_targets:
        try:
            result = fetch_one(
                target,
                auth_args=auth_args,
                visibility_override=args.visibility,
                title_override=args.title,
                force=args.force,
            )
            results.append(result)
            if result.get("skipped"):
                print(f"Skip {result['id']}: {result['reason']}")
            else:
                wrote_any = True
                print(
                    f"Fetched {result['id']}: {result['lines']} lines -> {result['inboxPath']} "
                    f"({result['visibility']})"
                )
        except Exception as exc:  # noqa: BLE001
            video_id = extract_video_id(target)
            message = str(exc)
            if is_members_only_error(message):
                mark_catalog_visibility(video_id, "members-only")
                message = (
                    f"{message}\nMarked {video_id} as members-only in catalog. "
                    "Re-run with working browser cookies, or use clipboard_to_inbox.py."
                )
            failures.append({"id": video_id, "error": message})
            print(f"FAIL {video_id}: {message}", file=sys.stderr)

    if wrote_any and not args.no_ingest:
        print("Ingesting inbox...")
        run_ingest(rebuild=not args.no_rebuild)

    if failures:
        print(
            "\nClipboard/cookies fallback for failed videos:\n"
            "  1) Export data/youtube.cookies.txt using docs/cookies-setup.md, then rerun\n"
            "  2) Or Merlin copy + py scripts/clipboard_to_inbox.py --url \"...\" --ingest",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
