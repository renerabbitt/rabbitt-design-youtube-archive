# YouTube Repository

This repo stores YouTube channel content so it can be searched, summarized, indexed by topic, and published as a website.

## Goals

- Keep a list of every channel video with title, URL, publish date, description, tags, and transcript status.
- Store transcripts in plain text or Markdown so they are easy to review and regenerate.
- Create summaries, chapters, keywords, and topic indexes from each transcript.
- Build a GitHub-hosted search website that embeds videos and helps visitors find relevant content.
- Keep the content portable so it can later be reused on Squarespace for SEO pages.

## Suggested Workflow

### Preferred: auto-fetch captions (no Merlin)

Stay logged into YouTube in Chrome, then:

```powershell
# One video
py scripts/fetch_transcripts.py --url "https://www.youtube.com/watch?v=VIDEO_ID"

# Next batch of catalog gaps
py scripts/fetch_transcripts.py --pending --limit 10
```

That command:

- Pulls YouTube captions via `yt-dlp` (uses browser cookies by default for members-only)
- Writes `data/inbox/<id>.txt`
- Runs ingest: transcript + draft summary + catalog upsert + search index rebuild

For public videos you can skip cookies: `--browser none`.

### Members-only / VIP videos

Public caption fetch cannot see VIP videos without cookies, and Chrome cookie decryption often fails on Windows.

**Working method:** use the already-logged-in Cursor browser session.

1. Keep Cursor browser signed into the channel owner account.
2. Start the local receiver:

```powershell
py scripts/browser_transcript_receiver.py
```

3. Open a VIP watch URL in that browser and run the extract script in [`scripts/youtube_browser_transcript.js`](scripts/youtube_browser_transcript.js) (agent does this automatically): it toggles captions, intercepts the player `timedtext` request (needs the `pot` token), and POSTs the transcript to `http://127.0.0.1:8765/ingest`.
4. Then:

```powershell
py scripts/ingest_video.py --process-inbox
```

Cookie-file export remains an optional fallback only.

## Refreshing The Video List

Export channel metadata with `yt-dlp`, then normalize it:

```powershell
py -m yt_dlp --flat-playlist --dump-single-json "https://www.youtube.com/@rabbittdesign8482/videos" | Out-File -Encoding utf8 "data/channel-videos.raw.json"
py scripts/import_youtube_catalog.py
```

## Building The Search Website

Generate the static search index:

```powershell
py scripts/build_site_data.py
```

Preview the website locally:

```powershell
py -m http.server 4173 --directory "site"
```

Then open:

```text
http://localhost:4173/
```

The current site is a GitHub Pages-compatible static site in `site/`. It includes:

- Chapter and subchapter browsing.
- Search across titles, summaries, topics, keywords, chapter titles, and full transcript text.
- Video cards with YouTube embeds and timestamp chapter links.
- Shared taxonomy in `data/taxonomy.json` used by both ingest and site build.

Important: several imported transcripts are members-only/VIP content. Publish only when you are comfortable making that content searchable.

## Fast Path For Future Videos

1. `py scripts/fetch_transcripts.py --url "..."` (or `--pending`)
2. Only if that fails: Merlin copy → `py scripts/clipboard_to_inbox.py --url "..." --ingest`

AI should spend credits on:

- Fixing bad auto-chapters
- Improving SEO page copy
- Expanding taxonomy terms

AI should **not** spend credits on:

- Re-typing transcripts into files
- Hand-building every chapter list
- Manual `videos.json` edits for each new video
- Pasting Merlin transcripts into chat when fetch/clipboard scripts can do it

## Hosting Direction

GitHub Pages is the easiest first version because it can host a static searchable site for free. Squarespace is probably better for SEO if the final goal is to bring search traffic back to your main website, but it may require one of these approaches:

- Create Squarespace pages manually from the generated summaries and chapter indexes.
- Embed the GitHub search app inside a Squarespace page.
- Generate static SEO pages that are copied into Squarespace.
- Use Squarespace only as the public landing page and link out to the GitHub-hosted searchable archive.

The repo should keep the content and index generation independent from the hosting choice.
