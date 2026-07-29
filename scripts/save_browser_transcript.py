"""
Save a browser-extracted YouTube transcript JSON into data/inbox/ and ingest.

Expected JSON shape (from scripts/youtube_browser_transcript.js):

{
  "ok": true,
  "videoId": "...",
  "title": "...",
  "url": "...",
  "transcript": "0:00 line\\n0:03 line",
  "lineCount": 123
}

Usage:

    py scripts/save_browser_transcript.py path/to/result.json --ingest
    py scripts/save_browser_transcript.py --stdin --ingest
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INBOX_DIR = ROOT / "data" / "inbox"


def write_inbox(payload: dict, visibility: str = "members-only") -> Path:
    if not payload.get("ok"):
        raise ValueError(payload.get("reason") or "extract failed")
    video_id = payload.get("videoId")
    title = (payload.get("title") or video_id or "Untitled").strip()
    url = payload.get("url") or f"https://www.youtube.com/watch?v={video_id}"
    transcript = (payload.get("transcript") or "").strip()
    if not video_id:
        raise ValueError("videoId missing")
    if len(transcript.splitlines()) < 3:
        raise ValueError("transcript too short")

    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    path = INBOX_DIR / f"{video_id}.txt"
    path.write_text(
        f"Title: {title}\nURL: {url}\nVisibility: {visibility}\n\n{transcript}\n",
        encoding="utf-8",
    )
    return path


def run_ingest(rebuild: bool = True) -> None:
    cmd = [sys.executable, str(ROOT / "scripts" / "ingest_video.py"), "--process-inbox"]
    if not rebuild:
        cmd.append("--no-rebuild")
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.returncode != 0:
        raise RuntimeError(result.stderr or result.stdout or "ingest failed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", nargs="?")
    parser.add_argument("--stdin", action="store_true")
    parser.add_argument("--visibility", default="members-only")
    parser.add_argument("--ingest", action="store_true")
    parser.add_argument("--no-rebuild", action="store_true")
    args = parser.parse_args()

    if args.stdin:
        payload = json.load(sys.stdin)
    elif args.json_file:
        payload = json.loads(Path(args.json_file).read_text(encoding="utf-8"))
        # Support raw CDP envelopes.
        if "result" in payload and isinstance(payload["result"], dict):
            nested = payload["result"]
            if "value" in nested:
                payload = nested["value"]
            elif "result" in nested and isinstance(nested["result"], dict) and "value" in nested["result"]:
                payload = nested["result"]["value"]
    else:
        parser.error("Provide json_file or --stdin")

    path = write_inbox(payload, visibility=args.visibility)
    print(f"Wrote {path.relative_to(ROOT)} ({payload.get('lineCount')} lines)")
    if args.ingest:
        run_ingest(rebuild=not args.no_rebuild)


if __name__ == "__main__":
    main()
