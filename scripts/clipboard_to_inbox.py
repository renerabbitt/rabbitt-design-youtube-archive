"""
Save a Merlin (or other) clipboard transcript into data/inbox/ and optionally ingest.

Usage:

    # Copy transcript in Merlin, then:
    py scripts/clipboard_to_inbox.py --url "https://www.youtube.com/live/VIDEO_ID" --ingest

    # Or copy title+url+transcript together in the inbox format / chat paste format:
    py scripts/clipboard_to_inbox.py --ingest
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

try:
    import pyperclip
except ImportError:  # pragma: no cover
    pyperclip = None

ROOT = Path(__file__).resolve().parents[1]
INBOX_DIR = ROOT / "data" / "inbox"

URL_RE = re.compile(
    r"(?:https?://)?(?:www\.)?(?:youtube\.com/(?:watch\?v=|live/|shorts/)|youtu\.be/)([A-Za-z0-9_-]{11})"
)
TIMESTAMP_RE = re.compile(r"^(?:(?:\d{1,2}:)?\d{1,2}:\d{2})\s+\S+")


def read_clipboard() -> str:
    if pyperclip is not None:
        text = pyperclip.paste() or ""
        if text.strip():
            return text
    # PowerShell fallback on Windows.
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", "Get-Clipboard -Raw"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr or "Could not read clipboard")
    return result.stdout or ""


def extract_video_id(value: str) -> str:
    match = URL_RE.search(value.strip())
    if match:
        return match.group(1)
    value = value.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", value):
        return value
    raise ValueError(f"Could not find a YouTube video id in: {value}")


def looks_like_transcript(text: str) -> bool:
    timed = sum(1 for line in text.splitlines() if TIMESTAMP_RE.match(line.strip()))
    return timed >= 3


def build_inbox_payload(
    clipboard: str,
    url: str | None,
    title: str | None,
    visibility: str,
) -> tuple[str, str]:
    text = clipboard.lstrip("\ufeff").strip()
    if not text:
        raise ValueError("Clipboard is empty")

    # Full inbox / chat paste already includes headers.
    lower = text.lower()
    if lower.startswith("title:") or (URL_RE.search("\n".join(text.splitlines()[:4])) and looks_like_transcript(text)):
        # Ensure URL/title overrides win when provided.
        lines = text.splitlines()
        meta: dict[str, str] = {}
        body_start = 0
        first = lines[0]
        if ":" in first and first.split(":", 1)[0].strip().lower() in {
            "title",
            "url",
            "visibility",
            "duration",
            "durationseconds",
        }:
            for index, line in enumerate(lines):
                if not line.strip():
                    body_start = index + 1
                    break
                if ":" not in line:
                    body_start = index
                    break
                key, value = line.split(":", 1)
                key_norm = key.strip().lower()
                if key_norm not in {"title", "url", "visibility", "duration", "durationseconds"}:
                    body_start = index
                    break
                meta[key_norm] = value.strip()
            else:
                body_start = len(lines)
            final_title = title or meta.get("title") or "Untitled video"
            final_url = url or meta.get("url")
            final_visibility = meta.get("visibility") or visibility
            body = "\n".join(lines[body_start:]).strip()
        else:
            # Title\nURL\n\ntranscript
            final_title = title or lines[0].strip()
            final_url = url or (lines[1].strip() if len(lines) > 1 else None)
            body_start = 2
            if body_start < len(lines) and not lines[body_start].strip():
                body_start += 1
            body = "\n".join(lines[body_start:]).strip()
            final_visibility = visibility

        if not final_url:
            raise ValueError("URL is required (pass --url or include it in the clipboard paste)")
        if not looks_like_transcript(body):
            raise ValueError("Clipboard does not look like a timed transcript")
        video_id = extract_video_id(final_url)
        payload = (
            f"Title: {final_title}\n"
            f"URL: {final_url if final_url.startswith('http') else f'https://www.youtube.com/watch?v={video_id}'}\n"
            f"Visibility: {final_visibility}\n"
            f"\n"
            f"{body}\n"
        )
        return video_id, payload

    # Transcript-only clipboard: require --url
    if not url:
        raise ValueError(
            "Clipboard looks like transcript-only text. Pass --url "
            '(and optional --title), e.g. --url "https://www.youtube.com/live/VIDEO_ID"'
        )
    if not looks_like_transcript(text):
        raise ValueError("Clipboard does not look like a timed transcript (expected lines like '0:00 text')")

    video_id = extract_video_id(url)
    final_title = title or f"YouTube video {video_id}"
    watch_url = url if url.startswith("http") else f"https://www.youtube.com/watch?v={video_id}"
    payload = (
        f"Title: {final_title}\n"
        f"URL: {watch_url}\n"
        f"Visibility: {visibility}\n"
        f"\n"
        f"{text}\n"
    )
    return video_id, payload


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
    parser = argparse.ArgumentParser(description="Write clipboard transcript to data/inbox/.")
    parser.add_argument("--url", help="YouTube URL or video id (required for transcript-only clipboard)")
    parser.add_argument("--title", help="Video title override")
    parser.add_argument("--visibility", default="members-only")
    parser.add_argument("--ingest", action="store_true", help="Run ingest after writing inbox file")
    parser.add_argument("--no-rebuild", action="store_true")
    args = parser.parse_args()

    clipboard = read_clipboard()
    video_id, payload = build_inbox_payload(clipboard, args.url, args.title, args.visibility)
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    path = INBOX_DIR / f"{video_id}.txt"
    path.write_text(payload, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)} ({len(payload.splitlines())} lines)")

    if args.ingest:
        print("Ingesting inbox...")
        run_ingest(rebuild=not args.no_rebuild)


if __name__ == "__main__":
    main()
