"""Download audio + Whisper for catalog videos missing captions."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIO_DIR = ROOT / "data" / "inbox" / "_meta" / "audio"
INBOX = ROOT / "data" / "inbox"
REMAINING = ROOT / "data" / "inbox" / "_meta" / "_public_remaining.txt"
VIDEOS_JSON = ROOT / "data" / "videos.json"


def format_ts(seconds: float) -> str:
    total = max(0, int(seconds))
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def load_catalog() -> dict[str, dict]:
    data = json.loads(VIDEOS_JSON.read_text(encoding="utf-8"))
    return {v["id"]: v for v in data["videos"]}


def missing_ids(catalog: dict[str, dict]) -> list[str]:
    out = []
    for vid, v in catalog.items():
        tp = v.get("transcriptPath")
        if tp and (ROOT / tp).exists():
            continue
        out.append(vid)
    if REMAINING.exists():
        prefer = [
            ln.strip()
            for ln in REMAINING.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.startswith("#")
        ]
        prefer_set = set(prefer)
        ordered = [i for i in prefer if i in set(out)]
        ordered += [i for i in out if i not in prefer_set]
        return ordered
    return out


def download_audio(video_id: str) -> Path:
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    dest = AUDIO_DIR / f"{video_id}.mp3"
    if dest.exists() and dest.stat().st_size > 1000:
        return dest
    url = f"https://www.youtube.com/watch?v={video_id}"
    cmd = [
        sys.executable,
        "-m",
        "yt_dlp",
        "-f",
        "bestaudio/best",
        "-x",
        "--audio-format",
        "mp3",
        "--audio-quality",
        "5",
        "-o",
        str(AUDIO_DIR / "%(id)s.%(ext)s"),
        "--no-playlist",
        url,
    ]
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
    if result.returncode != 0 or not dest.exists():
        raise RuntimeError((result.stderr or result.stdout or "yt_dlp failed").strip()[-500:])
    return dest


def run_whisper(audio: Path, model: str = "tiny") -> Path:
    out_json = audio.with_suffix(".json")
    if out_json.exists() and out_json.stat().st_size > 50:
        return out_json
    cmd = [
        "whisper",
        str(audio),
        "--model",
        model,
        "--output_format",
        "json",
        "--output_dir",
        str(audio.parent),
        "--language",
        "en",
        "--fp16",
        "False",
    ]
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
    if result.returncode != 0 or not out_json.exists():
        raise RuntimeError((result.stderr or result.stdout or "whisper failed").strip()[-800:])
    return out_json


def segments_to_lines(data: dict) -> list[str]:
    lines = []
    last = ""
    for seg in data.get("segments") or []:
        text = " ".join(str(seg.get("text") or "").split()).strip()
        if not text or text == last:
            continue
        last = text
        lines.append(f"{format_ts(float(seg.get('start') or 0))} {text}")
    return lines


def write_inbox(video_id: str, title: str, visibility: str, lines: list[str]) -> Path:
    path = INBOX / f"{video_id}.txt"
    url = f"https://www.youtube.com/watch?v={video_id}"
    body = (
        f"Title: {title}\n"
        f"URL: {url}\n"
        f"Visibility: {visibility or 'public'}\n"
        f"Source: whisper\n\n"
        + "\n".join(lines)
        + "\n"
    )
    path.write_text(body, encoding="utf-8")
    return path


def update_remaining(done: set[str], pending: list[str]) -> None:
    left = [i for i in pending if i not in done]
    REMAINING.write_text(("\n".join(left) + ("\n" if left else "")), encoding="utf-8")


def main() -> None:
    model = "tiny"
    if len(sys.argv) > 1:
        model = sys.argv[1]
    catalog = load_catalog()
    pending = missing_ids(catalog)
    print(f"Missing: {len(pending)} model={model}")
    done: set[str] = set()
    failures: list[tuple[str, str]] = []
    for video_id in pending:
        meta = catalog.get(video_id) or {}
        title = meta.get("title") or video_id
        visibility = meta.get("visibility") or "public"
        print(f"=== {video_id}: {title[:60]}")
        try:
            audio = download_audio(video_id)
            print(f"  audio: {audio.name}")
            wjson = run_whisper(audio, model=model)
            data = json.loads(wjson.read_text(encoding="utf-8"))
            lines = segments_to_lines(data)
            if len(lines) < 2:
                # still write short marker transcript so catalog can mark ready
                text = " ".join(str(data.get("text") or "").split()).strip()
                if text:
                    lines = [f"0:00 {text}"]
                else:
                    raise RuntimeError("whisper produced empty transcript")
            path = write_inbox(video_id, title, visibility, lines)
            print(f"  wrote {path.name} ({len(lines)} lines)")
            done.add(video_id)
            update_remaining(done, pending)
        except Exception as exc:  # noqa: BLE001
            print(f"  FAIL: {exc}")
            failures.append((video_id, str(exc)))
            update_remaining(done, pending)

    if done:
        print("Ingesting inbox...")
        subprocess.run(
            [sys.executable, "scripts/ingest_video.py", "--process-inbox"],
            cwd=ROOT,
            check=False,
        )

    print(f"Done {len(done)} / {len(pending)}; failures {len(failures)}")
    for vid, err in failures:
        print(f"  {vid}: {err[:200]}")
    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
