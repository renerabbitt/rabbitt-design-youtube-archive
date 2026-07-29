const state = {
  data: null,
  query: "",
  subchapterId: "",
};

const elements = {
  stats: document.querySelector("#stats"),
  taxonomy: document.querySelector("#taxonomy"),
  results: document.querySelector("#results"),
  resultsTitle: document.querySelector("#results-title"),
  resultsCount: document.querySelector("#results-count"),
  activeFilter: document.querySelector("#active-filter"),
  searchHelp: document.querySelector("#search-help"),
  searchForm: document.querySelector("#search-form"),
  searchInput: document.querySelector("#search-input"),
  clearFilter: document.querySelector("#clear-filter"),
  template: document.querySelector("#result-template"),
};

async function init() {
  const response = await fetch(`./search-index.json?ts=${Date.now()}`, { cache: "no-store" });
  state.data = await response.json();

  renderStats();
  renderTaxonomy();
  renderResults();
  elements.searchHelp.textContent = `Search currently covers ${state.data.stats.readyVideos} imported transcripts and summaries.`;

  elements.searchForm.addEventListener("submit", (event) => {
    event.preventDefault();
    state.query = elements.searchInput.value.trim();
    renderResults();
  });

  elements.searchInput.addEventListener("input", () => {
    state.query = elements.searchInput.value.trim();
    renderResults();
  });

  elements.clearFilter.addEventListener("click", () => {
    state.subchapterId = "";
    document.querySelectorAll(".chapter-button.active").forEach((button) => {
      button.classList.remove("active");
    });
    renderResults();
  });
}

function renderStats() {
  const { stats } = state.data;
  elements.stats.innerHTML = "";
  [
    ["Channel Videos", stats.totalVideos],
    ["Search Ready", stats.readyVideos],
    ["With Transcript", stats.transcriptVideos],
  ].forEach(([label, value]) => {
    const term = document.createElement("dt");
    term.textContent = label;
    const detail = document.createElement("dd");
    detail.textContent = value;
    elements.stats.append(term, detail);
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
      button.innerHTML = `${escapeHtml(subchapter.title)}<span>${count} indexed video${count === 1 ? "" : "s"}</span>`;
      button.addEventListener("click", () => {
        state.subchapterId = subchapter.id;
        document.querySelectorAll(".chapter-button.active").forEach((active) => {
          active.classList.remove("active");
        });
        button.classList.add("active");
        renderResults();
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
  const filter = findSubchapter(state.subchapterId);

  elements.resultsTitle.textContent = filter ? filter.title : "All Indexed Videos";
  elements.resultsCount.textContent = `${results.length} result${results.length === 1 ? "" : "s"}${queryLabel}`;

  if (filter) {
    elements.activeFilter.classList.remove("hidden");
    elements.activeFilter.textContent = `Filtering by ${filter.title}: ${filter.description}`;
  } else {
    elements.activeFilter.classList.add("hidden");
  }

  elements.results.innerHTML = "";

  if (!results.length) {
    const empty = document.createElement("p");
    empty.className = "muted";
    empty.textContent = "No videos match the current search and chapter filter.";
    elements.results.append(empty);
    return;
  }

  results.forEach((result) => {
    elements.results.append(renderVideoCard(result));
  });
}

function getResults() {
  const terms = normalizeTerms(state.query);
  const filtered = state.data.videos
    .map((video) => ({ video, score: scoreVideo(video, terms) }))
    .filter(({ video, score }) => {
      if (terms.length && !terms.every((term) => video.searchText.includes(term))) {
        return false;
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

  return terms.reduce((score, term) => {
    const matches = video.searchText.split(term).length - 1;
    return score + matches;
  }, 0);
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

  title.textContent = video.title;
  summary.textContent = firstParagraph(video.summary);
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
  if (!id) {
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
