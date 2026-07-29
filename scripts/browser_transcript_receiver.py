"""
Tiny local receiver for browser-extracted YouTube transcripts.

Start:

    py scripts/browser_transcript_receiver.py

Then in the logged-in Cursor browser, extract captions and POST JSON to:

    http://127.0.0.1:8765/ingest

Optional query: ?ingest=1 to also run inbox ingest after each save.
"""

from __future__ import annotations

import json
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
INBOX_DIR = ROOT / "data" / "inbox"
HOST = "127.0.0.1"
PORT = 8765


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


def run_ingest() -> str:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "ingest_video.py"), "--process-inbox"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr or result.stdout or "ingest failed")
    return result.stdout.strip()


class Handler(BaseHTTPRequestHandler):
    def _cors(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS, GET")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self) -> None:  # noqa: N802
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self) -> None:  # noqa: N802
        if self.path.startswith("/health"):
            body = b'{"ok":true}'
            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        self.send_response(404)
        self._cors()
        self.end_headers()

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path != "/ingest":
            self.send_response(404)
            self._cors()
            self.end_headers()
            return
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)
        try:
            payload = json.loads(raw.decode("utf-8"))
            visibility = "members-only"
            qs = parse_qs(parsed.query)
            if qs.get("visibility"):
                visibility = qs["visibility"][0]
            path = write_inbox(payload, visibility=visibility)
            response = {
                "ok": True,
                "inboxPath": str(path.relative_to(ROOT)),
                "videoId": payload.get("videoId"),
                "lineCount": payload.get("lineCount"),
            }
            if qs.get("ingest", ["0"])[0] in {"1", "true", "yes"}:
                response["ingest"] = run_ingest()
            body = json.dumps(response).encode("utf-8")
            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            print(f"saved {response['inboxPath']} ({response.get('lineCount')} lines)", flush=True)
        except Exception as exc:  # noqa: BLE001
            body = json.dumps({"ok": False, "error": str(exc)}).encode("utf-8")
            self.send_response(400)
            self._cors()
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            print(f"error: {exc}", flush=True)

    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"Listening on http://{HOST}:{PORT}/ingest", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
