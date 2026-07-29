import json
import time
import urllib.request

import websocket

version = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json/version").read())
pages = [
    t
    for t in json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json/list").read())
    if t.get("type") == "page"
]
print("pages", [(p.get("title"), p.get("url")) for p in pages[:5]])
ws = websocket.create_connection(version["webSocketDebuggerUrl"], timeout=20)
nid = 0


def call(method, params=None, session=None, timeout=30):
    global nid
    nid += 1
    msg = {"id": nid, "method": method, "params": params or {}}
    if session:
        msg["sessionId"] = session
    ws.send(json.dumps(msg))
    end = time.time() + timeout
    while time.time() < end:
        data = json.loads(ws.recv())
        if data.get("id") == nid:
            if "error" in data:
                raise RuntimeError(data["error"])
            return data.get("result", {})
    raise TimeoutError(method)


target = pages[0]["id"] if pages else call("Target.createTarget", {"url": "about:blank"})["targetId"]
sid = call("Target.attachToTarget", {"targetId": target, "flatten": True})["sessionId"]
call("Page.enable", session=sid)
call("Runtime.enable", session=sid)
call("Page.navigate", {"url": "https://www.youtube.com/@rabbittdesign8482"}, session=sid)
time.sleep(4)
expr = """(() => {
  const text = (document.body && document.body.innerText || '').slice(0, 3000);
  return {
    title: document.title,
    href: location.href,
    hasCustomize: /Customize channel/i.test(text),
    hasManage: /Manage videos/i.test(text),
    hasSignIn: /Sign in/i.test(text),
    snippet: text.slice(0, 800)
  };
})()"""
val = call(
    "Runtime.evaluate",
    {"expression": expr, "returnByValue": True},
    session=sid,
)
print(json.dumps(val.get("result", {}).get("value") or val, indent=2))
ws.close()
