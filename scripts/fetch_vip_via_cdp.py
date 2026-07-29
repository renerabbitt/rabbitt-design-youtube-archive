"""
Extract VIP/members-only YouTube captions via Chrome remote debugging.

Requires Chrome started with:
  chrome --remote-debugging-port=9222 --user-data-dir="<your Chrome profile>"

Usage:
  py scripts/fetch_vip_via_cdp.py --limit 10
  py scripts/fetch_vip_via_cdp.py --ids Vf5zVIZR0-s,xHE2WmpHFdM
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import websocket

ROOT = Path(__file__).resolve().parents[1]
VIDEOS_PATH = ROOT / "data" / "videos.json"
RECEIVER = "http://127.0.0.1:8765/ingest?ingest=0"
CDP_HTTP = "http://127.0.0.1:9222"

EXTRACT_JS = r"""
(async () => {
  for (let i=0;i<30;i++) {
    if (document.getElementById('movie_player') && window.ytInitialPlayerResponse) break;
    await new Promise(r => setTimeout(r, 200));
  }
  function formatTs(ms){
    const t=Math.max(0,Math.floor(ms/1000));
    const h=Math.floor(t/3600), m=Math.floor((t%3600)/60), s=t%60;
    return h ? `${h}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}` : `${m}:${String(s).padStart(2,'0')}`;
  }
  function json3ToLines(data){
    const lines=[]; let last='';
    for (const ev of data.events||[]) {
      if (!ev.segs) continue;
      const text=ev.segs.map(s=>s.utf8||'').join('').replace(/\n/g,' ').replace(/\s+/g,' ').trim();
      if (!text || text===last) continue;
      last=text;
      lines.push(`${formatTs(ev.tStartMs||0)} ${text}`);
    }
    return lines;
  }
  let payload=null;
  const OrigXHR=window.XMLHttpRequest;
  function WrappedXHR(){
    const xhr=new OrigXHR();
    const open=xhr.open;
    xhr.open=function(method,url,...rest){ this.__url=String(url); return open.call(this,method,url,...rest); };
    xhr.addEventListener('load', function(){
      const url=this.__url||'';
      if (/timedtext/i.test(url) && (this.responseText||'').length>1000) {
        try { payload=JSON.parse(this.responseText); } catch(e) {}
      }
    });
    return xhr;
  }
  window.XMLHttpRequest=WrappedXHR;
  const p=document.getElementById('movie_player');
  if (!p) return {ok:false, reason:'no player'};
  try { p.playVideo(); p.mute(); } catch(e) {}
  try { if (p.isSubtitlesOn && p.isSubtitlesOn()) p.toggleSubtitles(); } catch(e) {}
  await new Promise(r => setTimeout(r, 400));
  try { p.toggleSubtitlesOn(); } catch(e) { try { p.toggleSubtitles(); } catch(e2) {} }
  for (let i=0;i<12 && !payload;i++) {
    await new Promise(r => setTimeout(r, 700));
    try { p.seekTo(Math.min(5+i*15, 200), true); } catch(e) {}
  }
  window.XMLHttpRequest=OrigXHR;
  if (!payload) {
    const tracks=window.ytInitialPlayerResponse?.captions?.playerCaptionsTracklistRenderer?.captionTracks||[];
    return {ok:false, reason:'no timedtext', trackCount: tracks.length, title: document.title};
  }
  const lines=json3ToLines(payload);
  const result={
    ok: lines.length>=3,
    videoId: new URL(location.href).searchParams.get('v'),
    title: (document.title||'').replace(/ - YouTube$/i,'').replace(/^\(\d+\)\s*/,''),
    url: location.href,
    lineCount: lines.length,
    transcript: lines.join('\n')
  };
  const res=await fetch('RECEIVER_URL', {
    method:'POST',
    headers:{'content-type':'application/json'},
    body: JSON.stringify(result)
  });
  let save=null;
  try { save=await res.json(); } catch(e) { save={ok:false, error:String(e)}; }
  return {extractOk: result.ok, lineCount: result.lineCount, title: result.title, videoId: result.videoId, save};
})()
""".replace("RECEIVER_URL", RECEIVER)


class CDP:
    def __init__(self, ws_url: str):
        self.ws = websocket.create_connection(ws_url, timeout=30)
        self._id = 0

    def call(self, method: str, params: dict | None = None, session_id: str | None = None, timeout: float = 60):
        self._id += 1
        msg = {"id": self._id, "method": method, "params": params or {}}
        if session_id:
            msg["sessionId"] = session_id
        self.ws.send(json.dumps(msg))
        deadline = time.time() + timeout
        while time.time() < deadline:
            raw = self.ws.recv()
            data = json.loads(raw)
            if data.get("id") == self._id:
                if "error" in data:
                    raise RuntimeError(data["error"])
                return data.get("result", {})
        raise TimeoutError(method)

    def close(self):
        try:
            self.ws.close()
        except Exception:
            pass


def http_json(url: str):
    with urllib.request.urlopen(url, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


def list_pages():
    return [t for t in http_json(f"{CDP_HTTP}/json/list") if t.get("type") == "page"]


def pending_members(limit: int, ids: list[str] | None = None) -> list[dict]:
    catalog = json.loads(VIDEOS_PATH.read_text(encoding="utf-8"))
    pending = [
        v
        for v in catalog.get("videos", [])
        if v.get("visibility") == "members-only" and v.get("status") != "ready"
    ]
    if ids:
        wanted = set(ids)
        pending = [v for v in pending if v["id"] in wanted] + [
            {"id": i, "title": i, "url": f"https://www.youtube.com/watch?v={i}"}
            for i in ids
            if i not in {v["id"] for v in pending}
        ]
    return pending[:limit]


def ensure_receiver() -> None:
    try:
        urllib.request.urlopen("http://127.0.0.1:8765/health", timeout=2)
    except Exception:
        subprocess.Popen(
            [sys.executable, str(ROOT / "scripts" / "browser_transcript_receiver.py")],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        time.sleep(1)


def extract_one(cdp: CDP, session_id: str, video_id: str) -> dict:
    url = f"https://www.youtube.com/watch?v={video_id}"
    cdp.call("Page.navigate", {"url": url}, session_id=session_id)
    time.sleep(3)
    result = cdp.call(
        "Runtime.evaluate",
        {"expression": EXTRACT_JS, "awaitPromise": True, "returnByValue": True},
        session_id=session_id,
        timeout=90,
    )
    return result.get("result", {}).get("value") or result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--ids", help="Comma-separated video ids")
    parser.add_argument("--ingest", action="store_true")
    args = parser.parse_args()

    ensure_receiver()
    ids = [x.strip() for x in args.ids.split(",")] if args.ids else None
    targets = pending_members(args.limit, ids)
    if not targets:
        print("No pending members-only videos")
        return

    version = http_json(f"{CDP_HTTP}/json/version")
    browser_ws = version["webSocketDebuggerUrl"]
    cdp = CDP(browser_ws)
    try:
        # Prefer an existing page target; otherwise create one.
        pages = list_pages()
        if pages:
            target_id = pages[0]["id"]
        else:
            created = cdp.call("Target.createTarget", {"url": "about:blank"})
            target_id = created["targetId"]
        attached = cdp.call("Target.attachToTarget", {"targetId": target_id, "flatten": True})
        session_id = attached["sessionId"]
        cdp.call("Page.enable", session_id=session_id)
        cdp.call("Runtime.enable", session_id=session_id)

        ok = 0
        fail = 0
        for video in targets:
            video_id = video["id"]
            try:
                value = extract_one(cdp, session_id, video_id)
                if value.get("extractOk") or (value.get("save") or {}).get("ok"):
                    ok += 1
                    print(f"OK {video_id}: {value.get('lineCount')} lines - {value.get('title')}")
                else:
                    fail += 1
                    print(f"FAIL {video_id}: {value}")
            except Exception as exc:  # noqa: BLE001
                fail += 1
                print(f"FAIL {video_id}: {exc}")
        print(f"Done ok={ok} fail={fail}")
    finally:
        cdp.close()

    if args.ingest:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "ingest_video.py"), "--process-inbox"],
            cwd=ROOT,
            check=False,
        )


if __name__ == "__main__":
    main()
