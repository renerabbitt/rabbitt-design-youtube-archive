/**
 * Extract a timed transcript from the currently open YouTube watch page.
 * Works for members-only/VIP when the Cursor browser session is logged in.
 *
 * Key insight: caption baseUrl from ytInitialPlayerResponse returns empty
 * without a player `pot` token. Toggle captions so the player XHRs timedtext
 * with pot, intercept that payload, convert json3 -> "M:SS text" lines.
 *
 * Usage in browser CDP Runtime.evaluate (awaitPromise=true): paste extractYouTubeTranscript.toString()
 * and invoke extractYouTubeTranscript().
 */
async function extractYouTubeTranscript() {
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
      // Skip pure sound markers like [Music] if desired? keep them for search.
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

  // Force a fresh caption request with pot token.
  try {
    if (p.isSubtitlesOn && p.isSubtitlesOn()) p.toggleSubtitles();
  } catch (e) {}
  await new Promise((r) => setTimeout(r, 500));
  try {
    p.toggleSubtitlesOn();
  } catch (e) {
    try {
      p.toggleSubtitles();
    } catch (e2) {}
  }

  for (let i = 0; i < 8 && !payload; i++) {
    await new Promise((r) => setTimeout(r, 700));
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
      reason: "no timedtext payload captured (captions may be unavailable)",
      title: document.title,
      url: location.href,
    };
  }

  const lines = json3ToLines(payload);
  const videoId = new URL(location.href).searchParams.get("v");
  return {
    ok: lines.length >= 3,
    videoId,
    title: (document.title || "").replace(/ - YouTube$/i, "").replace(/^\(\d+\)\s*/, ""),
    url: location.href,
    lineCount: lines.length,
    transcript: lines.join("\n"),
    reason: lines.length >= 3 ? null : "too few caption lines",
  };
}

extractYouTubeTranscript;
