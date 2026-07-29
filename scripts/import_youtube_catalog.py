import argparse
import json
from pathlib import Path


def normalize_catalog(raw_data: dict, channel_url: str, handle: str) -> dict:
    entries = raw_data.get("entries") or []
    videos = []

    for entry in entries:
        video_id = entry.get("id")
        if not video_id:
            continue

        thumbnails = entry.get("thumbnails") or []
        thumbnail = thumbnails[-1].get("url", "") if thumbnails else ""
        duration = entry.get("duration")

        videos.append(
            {
                "id": video_id,
                "title": entry.get("title") or "",
                "url": entry.get("url") or f"https://www.youtube.com/watch?v={video_id}",
                "publishedAt": "",
                "durationSeconds": duration if isinstance(duration, int) else None,
                "description": "",
                "tags": [],
                "topics": [],
                "viewCount": entry.get("view_count"),
                "thumbnail": thumbnail,
                "transcriptPath": f"data/transcripts/{video_id}.md",
                "summaryPath": f"data/summaries/{video_id}.md",
                "status": "needs-transcript",
            }
        )

    return {
        "channel": {
            "name": raw_data.get("channel") or raw_data.get("title") or "",
            "url": channel_url,
            "handle": handle,
            "id": raw_data.get("channel_id") or raw_data.get("id") or "",
        },
        "videos": videos,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Normalize yt-dlp channel metadata into data/videos.json."
    )
    parser.add_argument("--raw", default="data/channel-videos.raw.json")
    parser.add_argument("--out", default="data/videos.json")
    parser.add_argument("--channel-url", default="https://www.youtube.com/@rabbittdesign8482")
    parser.add_argument("--handle", default="@rabbittdesign8482")
    args = parser.parse_args()

    raw_path = Path(args.raw)
    out_path = Path(args.out)

    raw_data = json.loads(raw_path.read_text(encoding="utf-8-sig"))
    catalog = normalize_catalog(raw_data, args.channel_url, args.handle)

    out_path.write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(catalog['videos'])} videos to {out_path}")


if __name__ == "__main__":
    main()
