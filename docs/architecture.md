# Architecture Plan

## First Version

Build a static website that can be hosted on GitHub Pages.

The first version should:

- Load a generated search index from JSON.
- Search across video titles, descriptions, summaries, chapters, topics, keywords, and transcripts.
- Show matching videos with embedded YouTube players.
- Show matching chapters and summary snippets.
- Link back to the original YouTube video.

## Data Flow

1. `data/videos.json` tracks the canonical video list.
2. `data/transcripts/` stores one transcript per video.
3. `data/summaries/` stores one summary, topic list, keyword list, and chapter list per video.
4. A build script generates a compact `search-index.json`.
5. The static site reads `search-index.json` in the browser.

## Search Options

Recommended first implementation:

- Use client-side search with a small JavaScript search library such as Pagefind, Fuse.js, or Lunr.
- Keep all content static so GitHub Pages can host it without a server.
- Generate SEO-friendly pages per video and topic when the index is stable.

Later upgrade options:

- Use a hosted database or search service if the transcript library becomes too large for browser search.
- Generate dedicated topic pages for Squarespace.
- Embed the static search app in Squarespace while keeping GitHub as the content pipeline.

## Squarespace SEO Strategy

Squarespace is likely the better public destination if the goal is search traffic for your business website.

Possible strategy:

1. Use this repo as the content database and generator.
2. Generate one SEO page per video with summary, chapter links, embedded video, and related topics.
3. Generate topic pages that group related clips and videos.
4. Copy or sync those generated pages into Squarespace.
5. Keep GitHub Pages as a working archive and search prototype.

This keeps the source content clean and reusable while leaving the final publishing target flexible.
