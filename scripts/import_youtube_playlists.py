"""Fetch channel playlists + video membership into data/playlists.json."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CHANNEL = "https://www.youtube.com/@rabbittdesign8482/playlists"
DEFAULT_RAW = ROOT / "data" / "channel-playlists.raw.json"
DEFAULT_OUT = ROOT / "data" / "playlists.json"

# Prefer these near the top of the sidebar (user-called-out gaps).
PRIORITY_TITLE_PATTERNS = [
    re.compile(r"terrain", re.I),
    re.compile(r"\broof", re.I),
    re.compile(r"chief architect\s+shorts", re.I),
    re.compile(r"\bca\s+shorts", re.I),
]


def extract_json_payload(text: str) -> dict:
    """yt-dlp JSON may be preceded by PowerShell/stderr noise; find the object."""
    text = text.lstrip("\ufeff")
    start = text.find("{")
    if start < 0:
        raise ValueError("No JSON object found in yt-dlp output")
    return json.loads(text[start:])


def run_yt_dlp_json(url: str) -> dict:
    cmd = [
        sys.executable,
        "-m",
        "yt_dlp",
        "--flat-playlist",
        "--dump-single-json",
        "--no-warnings",
        url,
    ]
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    payload = (result.stdout or "").strip()
    if not payload and result.stderr:
        # Some hosts route deprecation text oddly; still try stderr.
        payload = result.stderr.strip()
    if result.returncode != 0 and not payload:
        raise RuntimeError(
            f"yt-dlp failed for {url} (exit {result.returncode}): {result.stderr.strip()}"
        )
    return extract_json_payload(payload)


def thumbnail_url(entry: dict) -> str:
    thumbs = entry.get("thumbnails") or []
    if not thumbs:
        return ""
    return thumbs[-1].get("url") or thumbs[0].get("url") or ""


def priority_rank(title: str) -> int:
    for index, pattern in enumerate(PRIORITY_TITLE_PATTERNS):
        if pattern.search(title or ""):
            return index
    return len(PRIORITY_TITLE_PATTERNS)


def normalize_playlist_meta(entry: dict) -> dict:
    playlist_id = entry.get("id") or ""
    url = entry.get("url") or (
        f"https://www.youtube.com/playlist?list={playlist_id}" if playlist_id else ""
    )
    return {
        "id": playlist_id,
        "title": (entry.get("title") or "").strip(),
        "url": url,
        "thumbnail": thumbnail_url(entry),
        "description": (entry.get("description") or "").strip(),
        "videoIds": [],
        "videoCount": 0,
    }


def fetch_playlist_video_ids(playlist_url: str) -> list[str]:
    data = run_yt_dlp_json(playlist_url)
    ids: list[str] = []
    seen: set[str] = set()
    for item in data.get("entries") or []:
        if not item:
            continue
        video_id = item.get("id")
        if not video_id or video_id in seen:
            continue
        # Skip nested playlist/url tabs if any leak through.
        if str(video_id).startswith("PL") and item.get("_type") in {"url", "playlist"}:
            continue
        seen.add(video_id)
        ids.append(video_id)
    return ids


def load_playlist_tab(raw_path: Path | None, channel_url: str, refresh: bool) -> dict:
    if refresh or not raw_path or not raw_path.exists():
        print(f"Fetching playlists tab: {channel_url}")
        data = run_yt_dlp_json(channel_url)
        if raw_path:
            raw_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path.write_text(
                json.dumps(data, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            print(f"Wrote raw dump to {raw_path}")
        return data

    print(f"Reading playlists tab from {raw_path}")
    return extract_json_payload(raw_path.read_text(encoding="utf-8-sig"))


def build_playlists(
    tab_data: dict,
    *,
    skip_videos: bool = False,
    limit: int | None = None,
) -> dict:
    channel = {
        "name": tab_data.get("channel") or tab_data.get("uploader") or "Rabbitt Design",
        "url": tab_data.get("channel_url")
        or tab_data.get("uploader_url")
        or "https://www.youtube.com/@rabbittdesign8482",
        "handle": tab_data.get("uploader_id") or "@rabbittdesign8482",
        "id": tab_data.get("channel_id") or tab_data.get("id") or "",
    }

    entries = [normalize_playlist_meta(entry) for entry in (tab_data.get("entries") or [])]
    entries = [entry for entry in entries if entry["id"]]
    entries.sort(key=lambda item: (priority_rank(item["title"]), item["title"].lower()))

    if limit is not None:
        entries = entries[:limit]

    playlists = []
    for index, playlist in enumerate(entries, start=1):
        if skip_videos:
            playlists.append(playlist)
            continue

        print(f"[{index}/{len(entries)}] Fetching videos: {playlist['title']}")
        try:
            video_ids = fetch_playlist_video_ids(playlist["url"])
        except Exception as exc:  # noqa: BLE001 - continue other playlists
            print(f"  WARN: failed ({exc})")
            video_ids = []

        playlist["videoIds"] = video_ids
        playlist["videoCount"] = len(video_ids)
        print(f"  {len(video_ids)} videos")
        playlists.append(playlist)

    return {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "channel": channel,
        "playlists": playlists,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Import YouTube channel playlists into data/playlists.json."
    )
    parser.add_argument("--channel-url", default=DEFAULT_CHANNEL)
    parser.add_argument("--raw", default=str(DEFAULT_RAW))
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Re-fetch the channel playlists tab even if a raw dump exists.",
    )
    parser.add_argument(
        "--skip-videos",
        action="store_true",
        help="Only import playlist titles/ids (no per-playlist video dump).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional cap on number of playlists to fetch (for testing).",
    )
    args = parser.parse_args()

    raw_path = Path(args.raw) if args.raw else None
    out_path = Path(args.out)

    tab_data = load_playlist_tab(raw_path, args.channel_url, refresh=args.refresh)
    catalog = build_playlists(tab_data, skip_videos=args.skip_videos, limit=args.limit)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(catalog['playlists'])} playlists to {out_path}")


if __name__ == "__main__":
    main()
