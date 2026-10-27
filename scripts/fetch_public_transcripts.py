"""Fetch missing public captions via youtube-transcript-api, then ingest once.

Install: python -m pip install -r requirements.txt
Run: python scripts/fetch_public_transcripts.py
Failures remain pending and are reported; existing transcripts are preserved.
"""

import argparse
import json
import time
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import IpBlocked, RequestBlocked

from fetch_transcripts import (
    ROOT, format_timestamp, pending_videos, run_ingest, write_inbox_file,
    is_members_only_error, mark_catalog_visibility,
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--delay", type=float, default=2)
    parser.add_argument("--report", type=Path, default=ROOT.parent / "caption-refresh-report.json")
    args = parser.parse_args()
    api = YouTubeTranscriptApi()
    targets = pending_videos(public_only=True)[:args.limit]
    report = {"fetched": [], "failures": [], "targetCount": len(targets)}
    try:
        for index, video in enumerate(targets):
            if index:
                time.sleep(max(0, args.delay))
            video_id = video["id"]
            try:
                captions = api.fetch(video_id, languages=["en"])
                lines = [f"{format_timestamp(c.start)} {c.text.replace(chr(10), ' ')}" for c in captions if c.text.strip()]
                if not lines:
                    raise ValueError("Empty captions")
                write_inbox_file(video_id, video["title"], video["url"], "public", "\n".join(lines))
                report["fetched"].append(video_id)
                print(f"[{index + 1}/{len(targets)}] Fetched {video_id}: {len(lines)} cues", flush=True)
            except Exception as exc:
                if is_members_only_error(str(exc)):
                    mark_catalog_visibility(video_id, "members-only")
                report["failures"].append({"id": video_id, "title": video["title"], "error": str(exc)})
                print(f"[{index + 1}/{len(targets)}] Failed {video_id}: {type(exc).__name__}", flush=True)
                if isinstance(exc, (IpBlocked, RequestBlocked)):
                    print("YouTube blocked requests; stopping this batch.", flush=True)
                    break
            finally:
                args.report.write_text(json.dumps(report, indent=2), encoding="utf-8")
    finally:
        if report["fetched"]:
            run_ingest()
    print(f"Fetched {len(report['fetched'])}; failed {len(report['failures'])}; report: {args.report}")


if __name__ == "__main__":
    main()
