const state = {
  data: null,
  query: "",
  subchapterId: "",
  playlistId: "",
};

const mobileQuery = window.matchMedia("(max-width: 980px)");

const elements = {
  stats: document.querySelector("#stats"),
  taxonomy: document.querySelector("#taxonomy"),
  taxonomyToggle: document.querySelector("#taxonomy-toggle"),
  taxonomyToggleHint: document.querySelector("#taxonomy-toggle-hint"),
  chaptersPanel: document.querySelector(".chapters-panel"),
  playlists: document.querySelector("#playlists"),
  playlistsToggle: document.querySelector("#playlists-toggle"),
  playlistsToggleHint: document.querySelector("#playlists-toggle-hint"),
  playlistsPanel: document.querySelector(".playlists-panel"),
  resultsSection: document.querySelector("#results-section"),
  results: document.querySelector("#results"),
  resultsTitle: document.querySelector("#results-title"),
  resultsCount: document.querySelector("#results-count"),
  activeFilter: document.querySelector("#active-filter"),
  searchHelp: document.querySelector("#search-help"),
  searchForm: document.querySelector("#search-form"),
  searchInput: document.querySelector("#search-input"),
  clearFilter: document.querySelector("#clear-filter"),
  clearPlaylistFilter: document.querySelector("#clear-playlist-filter"),
  template: document.querySelector("#result-template"),
};

function isMobileLayout() {
  return mobileQuery.matches;
}

function setPanelOpen(panel, toggle, open) {
  if (!panel || !toggle) {
    return;
  }
  panel.classList.toggle("is-collapsed", !open);
  toggle.setAttribute("aria-expanded", open ? "true" : "false");
}

function setTaxonomyOpen(open) {
  setPanelOpen(elements.chaptersPanel, elements.taxonomyToggle, open);
  updateTaxonomyToggleHint();
}

function setPlaylistsOpen(open) {
  setPanelOpen(elements.playlistsPanel, elements.playlistsToggle, open);
  updatePlaylistsToggleHint();
}

function updateTaxonomyToggleHint() {
  if (!elements.taxonomyToggleHint) {
    return;
  }
  const filter = findSubchapter(state.subchapterId);
  const open = elements.taxonomyToggle?.getAttribute("aria-expanded") === "true";
  if (filter) {
    elements.taxonomyToggleHint.textContent = open
      ? `Selected: ${filter.title}`
      : `${filter.title} · Tap to change`;
    return;
  }
  elements.taxonomyToggleHint.textContent = open
    ? "Pick a subchapter to filter videos"
    : "Tap to browse chapters";
}

function updatePlaylistsToggleHint() {
  if (!elements.playlistsToggleHint) {
    return;
  }
  const filter = findPlaylist(state.playlistId);
  const open = elements.playlistsToggle?.getAttribute("aria-expanded") === "true";
  if (filter) {
    elements.playlistsToggleHint.textContent = open
      ? `Selected: ${filter.title}`
      : `${filter.title} · Tap to change`;
    return;
  }
  elements.playlistsToggleHint.textContent = open
    ? "Pick a playlist to filter videos"
    : "Tap to browse playlists";
}

function clearActiveButtons(selector) {
  document.querySelectorAll(selector).forEach((button) => {
    button.classList.remove("active");
  });
}

function clearChapterFilter({ rerender = true } = {}) {
  state.subchapterId = "";
  clearActiveButtons("#taxonomy .chapter-button.active");
  updateTaxonomyToggleHint();
  if (rerender) {
    renderResults();
  }
}

function clearPlaylistFilter({ rerender = true } = {}) {
  state.playlistId = "";
  clearActiveButtons("#playlists .playlist-button.active");
  updatePlaylistsToggleHint();
  if (rerender) {
    renderResults();
  }
}

function revealResults() {
  const target = elements.activeFilter?.classList.contains("hidden")
    ? elements.resultsSection
    : elements.activeFilter;
  target?.scrollIntoView({ behavior: "smooth", block: "start" });
}

async function init() {
  const response = await fetch(`./search-index.json?ts=${Date.now()}`, { cache: "no-store" });
  state.data = await response.json();

  setTaxonomyOpen(!isMobileLayout());
  setPlaylistsOpen(!isMobileLayout());
  renderStats();
  renderPlaylists();
  renderTaxonomy();
  renderResults();
  elements.searchHelp.textContent = `Search covers ${state.data.stats.readyVideos} videos; ${state.data.stats.transcriptVideos} have full transcripts. Others are searchable by title and available metadata.`;

  elements.searchForm.addEventListener("submit", (event) => {
    event.preventDefault();
    state.query = elements.searchInput.value.trim();
    renderResults();
    if (isMobileLayout()) {
      revealResults();
    }
  });

  elements.searchInput.addEventListener("input", () => {
    state.query = elements.searchInput.value.trim();
    renderResults();
  });

  elements.clearFilter.addEventListener("click", () => {
    clearChapterFilter();
    if (isMobileLayout()) {
      setTaxonomyOpen(true);
    }
  });

  elements.clearPlaylistFilter?.addEventListener("click", () => {
    clearPlaylistFilter();
    if (isMobileLayout()) {
      setPlaylistsOpen(true);
    }
  });

  elements.taxonomyToggle?.addEventListener("click", () => {
    if (!isMobileLayout()) {
      return;
    }
    const open = elements.taxonomyToggle.getAttribute("aria-expanded") === "true";
    setTaxonomyOpen(!open);
  });

  elements.playlistsToggle?.addEventListener("click", () => {
    if (!isMobileLayout()) {
      return;
    }
    const open = elements.playlistsToggle.getAttribute("aria-expanded") === "true";
    setPlaylistsOpen(!open);
  });

  const syncLayoutMode = () => {
    if (isMobileLayout()) {
      setTaxonomyOpen(false);
      setPlaylistsOpen(false);
    } else {
      setTaxonomyOpen(true);
      setPlaylistsOpen(true);
    }
  };
  if (typeof mobileQuery.addEventListener === "function") {
    mobileQuery.addEventListener("change", syncLayoutMode);
  } else if (typeof mobileQuery.addListener === "function") {
    mobileQuery.addListener(syncLayoutMode);
  }
}

function renderStats() {
  const { stats } = state.data;
  elements.stats.innerHTML = "";
  [
    ["Channel Videos", stats.totalVideos],
    ["Search Ready", stats.readyVideos],
    ["With Transcript", stats.transcriptVideos],
    ["Playlists", stats.playlistCount ?? (state.data.playlists || []).length],
  ].forEach(([label, value]) => {
    const term = document.createElement("dt");
    term.textContent = label;
    const detail = document.createElement("dd");
    detail.textContent = value;
    elements.stats.append(term, detail);
  });
}

function renderPlaylists() {
  if (!elements.playlists) {
    return;
  }
  elements.playlists.innerHTML = "";
  const playlists = state.data.playlists || [];

  if (!playlists.length) {
    const empty = document.createElement("p");
    empty.className = "muted";
    empty.textContent = "No playlists imported yet.";
    elements.playlists.append(empty);
    return;
  }

  playlists.forEach((playlist) => {
    const count = playlist.indexedCount ?? playlist.indexedVideoIds?.length ?? 0;
    const total = playlist.videoCount ?? playlist.videoIds?.length ?? 0;
    const button = document.createElement("button");
    button.className = "chapter-button playlist-button";
    button.type = "button";
    button.dataset.playlistId = playlist.id;
    if (state.playlistId === playlist.id) {
      button.classList.add("active");
    }
    const countLabel =
      count === total
        ? `${count} indexed video${count === 1 ? "" : "s"}`
        : `${count} indexed · ${total} in playlist`;
    button.innerHTML = `${escapeHtml(playlist.title)}<span>${escapeHtml(countLabel)}</span>`;
    button.addEventListener("click", () => {
      clearChapterFilter({ rerender: false });
      state.playlistId = playlist.id;
      clearActiveButtons("#playlists .playlist-button.active");
      button.classList.add("active");
      renderResults();
      updatePlaylistsToggleHint();
      if (isMobileLayout()) {
        setPlaylistsOpen(false);
        setTaxonomyOpen(false);
        revealResults();
      }
    });
    elements.playlists.append(button);
  });
}

function renderTaxonomy() {
  elements.taxonomy.innerHTML = "";

  state.data.taxonomy.forEach((chapter) => {
    const group = document.createElement("section");
    group.className = "chapter-group";

    const title = document.createElement("h3");
    title.textContent = chapter.title;

    const description = document.createElement("p");
    description.textContent = chapter.description;

    const list = document.createElement("div");
    list.className = "subchapter-list";

    chapter.subchapters.forEach((subchapter) => {
      const count = subchapter.videoIds?.length || 0;
      const button = document.createElement("button");
      button.className = "chapter-button";
      button.type = "button";
      button.dataset.subchapterId = subchapter.id;
      if (state.subchapterId === subchapter.id) {
        button.classList.add("active");
      }
      button.innerHTML = `${escapeHtml(subchapter.title)}<span>${count} indexed video${count === 1 ? "" : "s"}</span>`;
      button.addEventListener("click", () => {
        clearPlaylistFilter({ rerender: false });
        state.subchapterId = subchapter.id;
        clearActiveButtons("#taxonomy .chapter-button.active");
        button.classList.add("active");
        renderResults();
        updateTaxonomyToggleHint();
        if (isMobileLayout()) {
          setTaxonomyOpen(false);
          setPlaylistsOpen(false);
          revealResults();
        }
      });
      list.append(button);
    });

    group.append(title, description, list);
    elements.taxonomy.append(group);
  });
}

function renderResults() {
  const results = getResults();
  const queryLabel = state.query ? ` for "${state.query}"` : "";
  const chapterFilter = findSubchapter(state.subchapterId);
  const playlistFilter = findPlaylist(state.playlistId);
  const filter = playlistFilter || chapterFilter;

  elements.resultsTitle.textContent = filter ? filter.title : "All Indexed Videos";
  elements.resultsCount.textContent = `${results.length} result${results.length === 1 ? "" : "s"}${queryLabel}`;

  if (playlistFilter) {
    elements.activeFilter.classList.remove("hidden");
    const total = playlistFilter.videoCount ?? playlistFilter.videoIds?.length ?? 0;
    const indexed = playlistFilter.indexedCount ?? playlistFilter.indexedVideoIds?.length ?? 0;
    elements.activeFilter.textContent = `Filtering by playlist ${playlistFilter.title} (${indexed} indexed of ${total} videos).`;
  } else if (chapterFilter) {
    elements.activeFilter.classList.remove("hidden");
    elements.activeFilter.textContent = `Filtering by ${chapterFilter.title}: ${chapterFilter.description}`;
  } else {
    elements.activeFilter.classList.add("hidden");
  }

  updateTaxonomyToggleHint();
  updatePlaylistsToggleHint();

  elements.results.innerHTML = "";

  if (!results.length) {
    const empty = document.createElement("p");
    empty.className = "muted";
    empty.textContent = "No videos match the current search and filter.";
    elements.results.append(empty);
    return;
  }

  results.forEach((result) => {
    elements.results.append(renderVideoCard(result));
  });
}

function getResults() {
  const terms = normalizeTerms(state.query);
  const playlist = findPlaylist(state.playlistId);
  const playlistIdSet = playlist
    ? new Set(playlist.videoIds || playlist.indexedVideoIds || [])
    : null;

  const filtered = state.data.videos
    .map((video) => ({ video, score: scoreVideo(video, terms) }))
    .filter(({ video }) => {
      if (terms.length && !terms.every((term) => video.searchText.includes(term))) {
        return false;
      }
      if (playlistIdSet) {
        return playlistIdSet.has(video.id) || (video.playlistIds || []).includes(state.playlistId);
      }
      if (!state.subchapterId) {
        return true;
      }
      return video.chapters.some((chapter) => chapter.subchapterId === state.subchapterId);
    });

  return filtered
    .sort((a, b) => b.score - a.score || a.video.title.localeCompare(b.video.title))
    .map(({ video }) => video);
}

function scoreVideo(video, terms) {
  if (!terms.length) {
    return 1;
  }

  const title = video.title.toLowerCase();
  const phraseBonus = title.includes(terms.join(" ")) ? 200 : 0;
  return terms.reduce((score, term) => {
    const matches = video.searchText.split(term).length - 1;
    return score + Math.min(matches, 20) + (title.includes(term) ? 10 : 0);
  }, phraseBonus);
}

function renderVideoCard(video) {
  const node = elements.template.content.firstElementChild.cloneNode(true);
  const embed = node.querySelector(".video-embed");
  const meta = node.querySelector(".video-meta");
  const title = node.querySelector("h3");
  const summary = node.querySelector(".summary");
  const actions = node.querySelector(".card-actions");
  const tags = node.querySelector(".tags");
  const chapters = node.querySelector(".matching-chapters");
  const snippet = node.querySelector(".snippet");

  const membersOnly = isMembersOnly(video);

  if (membersOnly) {
    embed.append(createMembersOnlyPlaceholder(video));
  } else if (video.embedUrl) {
    embed.append(createLazyEmbed(video));
  }

  meta.append(createBadge(formatDuration(video.durationSeconds)));
  meta.append(createBadge(membersOnly ? "Members Only" : "Public", membersOnly));
  if (video.transcriptAvailable === false) {
    meta.append(createBadge("Transcript pending"));
  }

  title.textContent = video.title;
  summary.textContent = firstParagraph(video.summary) || (video.transcriptAvailable === false
    ? "Searchable by title. Full transcript search is pending."
    : "");
  actions.append(
    createActionLink("Rabbitt Design Videos", "https://www.rabbittdesign.net/videos", true),
    createActionLink("Chief Search", "https://www.rabbittdesign.net/chiefsearch"),
    createActionLink(membersOnly ? "Watch on YouTube" : "Open YouTube", video.url)
  );

  [...video.topics.slice(0, 8), ...video.keywords.slice(0, 4)].forEach((tag) => {
    const item = document.createElement("span");
    item.className = "tag";
    item.textContent = tag;
    tags.append(item);
  });

  const visibleChapters = chaptersForVideo(video).slice(0, 8);
  if (visibleChapters.length) {
    const heading = document.createElement("h4");
    heading.textContent = state.query ? "Best Matching Chapters" : "Chapters";
    chapters.append(heading);
  }

  visibleChapters.forEach((chapter) => {
    const link = document.createElement("a");
    link.className = "chapter-link";
    link.href = timestampUrl(video, chapter.seconds);
    link.target = "_blank";
    link.rel = "noreferrer";
    link.innerHTML = `<time>${escapeHtml(chapter.time)}</time> ${highlight(chapter.title, state.query)}`;
    chapters.append(link);
  });

  snippet.innerHTML = highlight(buildSnippet(video), state.query);
  node.querySelector("details").hidden = video.transcriptAvailable === false;
  return node;
}

function chaptersForVideo(video) {
  let chapters = video.chapters;
  if (state.subchapterId) {
    chapters = chapters.filter((chapter) => chapter.subchapterId === state.subchapterId);
  }

  const terms = normalizeTerms(state.query);
  if (!terms.length) {
    return chapters;
  }

  const directMatches = chapters.filter((chapter) => {
    const text = chapter.title.toLowerCase();
    return terms.some((term) => text.includes(term));
  });
  return directMatches.length ? directMatches : chapters;
}

function buildSnippet(video) {
  const terms = normalizeTerms(state.query);
  const text = video.transcript || video.summary || "";
  if (!terms.length) {
    return text.slice(0, 420) + (text.length > 420 ? "..." : "");
  }

  const lower = text.toLowerCase();
  const firstIndex = terms
    .map((term) => lower.indexOf(term))
    .filter((index) => index >= 0)
    .sort((a, b) => a - b)[0];

  if (firstIndex === undefined) {
    return firstParagraph(video.summary);
  }

  const start = Math.max(0, firstIndex - 180);
  const end = Math.min(text.length, firstIndex + 360);
  return `${start > 0 ? "..." : ""}${text.slice(start, end)}${end < text.length ? "..." : ""}`;
}

function normalizeTerms(query) {
  return query
    .toLowerCase()
    .split(/\s+/)
    .map((term) => term.trim())
    .filter((term) => term.length > 1);
}

function findSubchapter(id) {
  if (!id || !state.data) {
    return null;
  }
  for (const chapter of state.data.taxonomy) {
    const found = chapter.subchapters.find((subchapter) => subchapter.id === id);
    if (found) {
      return found;
    }
  }
  return null;
}

function findPlaylist(id) {
  if (!id || !state.data) {
    return null;
  }
  return (state.data.playlists || []).find((playlist) => playlist.id === id) || null;
}

function isMembersOnly(video) {
  const visibility = String(video?.visibility || "")
    .toLowerCase()
    .trim();
  return visibility === "members-only" || visibility === "member" || visibility === "vip";
}

function videoThumbnailUrl(video) {
  if (video?.thumbnail) {
    return video.thumbnail;
  }
  if (video?.id) {
    return `https://i.ytimg.com/vi/${video.id}/hqdefault.jpg`;
  }
  return "";
}

function createLazyEmbed(video) {
  const button = document.createElement("button");
  button.className = "video-poster";
  button.type = "button";
  button.setAttribute("aria-label", `Play ${video.title}`);

  const thumbUrl = videoThumbnailUrl(video);
  if (thumbUrl) {
    const image = document.createElement("img");
    image.className = "video-thumb";
    image.src = thumbUrl;
    image.alt = "";
    image.loading = "lazy";
    image.decoding = "async";
    image.addEventListener("error", () => {
      if (video.id && !image.dataset.fallback) {
        image.dataset.fallback = "1";
        image.src = `https://i.ytimg.com/vi/${video.id}/mqdefault.jpg`;
      } else {
        image.remove();
      }
    });
    button.append(image);
  }

  const overlay = document.createElement("span");
  overlay.className = "video-play-overlay";
  const play = document.createElement("span");
  play.className = "video-play-button";
  play.setAttribute("aria-hidden", "true");
  play.textContent = "▶";
  overlay.append(play);
  button.append(overlay);

  button.addEventListener("click", () => {
    const iframe = document.createElement("iframe");
    const embedUrl = new URL(video.embedUrl);
    embedUrl.searchParams.set("autoplay", "1");
    iframe.src = embedUrl.toString();
    iframe.title = video.title;
    iframe.allow =
      "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
    iframe.allowFullscreen = true;
    button.replaceWith(iframe);
  });

  return button;
}

function createMembersOnlyPlaceholder(video) {
  const link = document.createElement("a");
  link.className = "members-only-placeholder";
  link.href = video.url || `https://www.youtube.com/watch?v=${video.id}`;
  link.target = "_blank";
  link.rel = "noopener noreferrer";
  link.setAttribute("aria-label", `Members only. Watch ${video.title} on YouTube`);

  const thumbUrl = videoThumbnailUrl(video);
  if (thumbUrl) {
    const image = document.createElement("img");
    image.className = "members-only-thumb";
    image.src = thumbUrl;
    image.alt = "";
    image.loading = "lazy";
    image.decoding = "async";
    image.addEventListener("error", () => {
      if (video.id && !image.dataset.fallback) {
        image.dataset.fallback = "1";
        image.src = `https://i.ytimg.com/vi/${video.id}/mqdefault.jpg`;
      } else {
        image.remove();
      }
    });
    link.append(image);
  }

  const overlay = document.createElement("div");
  overlay.className = "members-only-overlay";

  const label = document.createElement("span");
  label.className = "members-only-label";
  label.textContent = "Members only";

  const cta = document.createElement("span");
  cta.className = "members-only-cta";
  cta.textContent = "Watch on YouTube";

  overlay.append(label, cta);
  link.append(overlay);
  return link;
}

function createBadge(text, warning = false) {
  const badge = document.createElement("span");
  badge.className = warning ? "badge warning" : "badge";
  badge.textContent = text;
  return badge;
}

function createActionLink(label, href, primary = false) {
  const link = document.createElement("a");
  link.href = href || "https://www.rabbittdesign.net/videos";
  link.target = "_blank";
  link.rel = "noopener noreferrer";
  link.textContent = label;
  if (primary) {
    link.className = "primary-link";
  }
  return link;
}

function firstParagraph(markdown) {
  return markdown
    .replace(/^# .+$/gm, "")
    .split(/\n\s*\n/)
    .map((part) => part.trim())
    .find(Boolean) || "";
}

function formatDuration(seconds) {
  if (!seconds) {
    return "Duration Unknown";
  }
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  if (hours) {
    return `${hours}h ${minutes}m`;
  }
  return `${minutes}m`;
}

function timestampUrl(video, seconds) {
  if (!video.url) {
    return "#";
  }
  const baseUrl = video.url.includes("youtube.com/live/")
    ? `https://www.youtube.com/watch?v=${video.id}`
    : video.url;
  const separator = baseUrl.includes("?") ? "&" : "?";
  return `${baseUrl}${separator}t=${seconds}s`;
}

function highlight(text, query) {
  const escaped = escapeHtml(text);
  const terms = normalizeTerms(query);
  if (!terms.length) {
    return escaped;
  }
  const pattern = new RegExp(`(${terms.map(escapeRegExp).join("|")})`, "gi");
  return escaped.replace(pattern, "<mark>$1</mark>");
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

init().catch((error) => {
  console.error(error);
  elements.results.innerHTML = `<p class="muted">Could not load the search index. Check the console for details.</p>`;
});
