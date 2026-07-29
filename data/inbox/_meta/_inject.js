/**
 * Extract pot-timedtext transcript from current YouTube watch page and POST to local receiver.
 * Returns a small status object (no full transcript) for CDP returnByValue.
 */
async function extractAndPostYouTubeTranscript(receiverUrl) {
  const endpoint = receiverUrl || "http://127.0.0.1:8765/ingest?ingest=0";

  function formatTs(ms) {
    const total = Math.max(0, Math.floor(ms / 1000));
    const h = Math.floor(total / 3600);
    const m = Math.floor((total % 3600) / 60);
    const s = total % 60;
    return h
      ? `${h}:${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`
      : `${m}:${String(s).padStart(2, "0")}`;
  }

  function json3ToLines(data) {
    const lines = [];
    let last = "";
    for (const ev of data.events || []) {
      if (!ev.segs) continue;
      const text = ev.segs
        .map((s) => s.utf8 || "")
        .join("")
        .replace(/\n/g, " ")
        .replace(/\s+/g, " ")
        .trim();
      if (!text || text === last) continue;
      last = text;
      lines.push(`${formatTs(ev.tStartMs || 0)} ${text}`);
    }
    return lines;
  }

  let payload = null;
  const OrigXHR = window.XMLHttpRequest;
  function WrappedXHR() {
    const xhr = new OrigXHR();
    const open = xhr.open;
    xhr.open = function (method, url, ...rest) {
      this.__url = String(url);
      return open.call(this, method, url, ...rest);
    };
    xhr.addEventListener("load", function () {
      const url = this.__url || "";
      if (/timedtext/i.test(url) && (this.responseText || "").length > 1000) {
        try {
          payload = JSON.parse(this.responseText);
          payload.__url = url;
        } catch (e) {
          payload = { raw: true, text: this.responseText, __url: url };
        }
      }
    });
    return xhr;
  }
  window.XMLHttpRequest = WrappedXHR;

  const p = document.getElementById("movie_player");
  if (!p) {
    return { ok: false, reason: "movie_player not found" };
  }

  try {
    p.playVideo();
  } catch (e) {}
  try {
    p.mute();
  } catch (e) {}

  try {
    if (p.isSubtitlesOn && p.isSubtitlesOn()) p.toggleSubtitles();
  } catch (e) {}
  await new Promise((r) => setTimeout(r, 400));
  try {
    p.toggleSubtitlesOn();
  } catch (e) {
    try {
      p.toggleSubtitles();
    } catch (e2) {}
  }

  for (let i = 0; i < 8 && !payload; i++) {
    await new Promise((r) => setTimeout(r, 600));
    if (!payload) {
      try {
        p.seekTo(Math.min(5 + i * 20, 120), true);
      } catch (e) {}
    }
  }

  window.XMLHttpRequest = OrigXHR;

  if (!payload || payload.raw) {
    return {
      ok: false,
      reason: "no timedtext payload captured",
      videoId: new URL(location.href).searchParams.get("v"),
      title: document.title,
    };
  }

  const lines = json3ToLines(payload);
  const videoId = new URL(location.href).searchParams.get("v");
  const title = (document.title || "")
    .replace(/ - YouTube$/i, "")
    .replace(/^\(\d+\)\s*/, "");

  if (lines.length < 3) {
    return { ok: false, reason: "too few caption lines", videoId, lineCount: lines.length };
  }

  const body = {
    ok: true,
    videoId,
    title,
    url: location.href,
    lineCount: lines.length,
    transcript: lines.join("\n"),
  };

  const res = await fetch(endpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const text = await res.text();
  let parsed = null;
  try {
    parsed = JSON.parse(text);
  } catch (e) {
    parsed = { raw: text };
  }

  return {
    ok: res.ok,
    videoId,
    title,
    lineCount: lines.length,
    status: res.status,
    receiver: parsed,
  };
}

window.__vipExtractAndPost = extractAndPostYouTubeTranscript;
