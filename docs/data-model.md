# Data Model

## Video Metadata

Each video in `data/videos.json` should use this shape:

```json
{
  "id": "youtube-video-id",
  "title": "Video title",
  "url": "https://www.youtube.com/watch?v=youtube-video-id",
  "publishedAt": "YYYY-MM-DD",
  "duration": "",
  "description": "",
  "tags": [],
  "topics": [],
  "transcriptPath": "data/transcripts/youtube-video-id.md",
  "summaryPath": "data/summaries/youtube-video-id.md",
  "status": "needs-transcript"
}
```

## Status Values

- `needs-transcript`: video exists, transcript has not been added.
- `needs-summary`: transcript exists, summary has not been created.
- `ready`: transcript and summary are ready for search and publishing.
- `skip`: video should not be included in the public index.

## Transcript Files

Transcript files should be Markdown and use this format:

```markdown
---
videoId: youtube-video-id
title: Video title
url: https://www.youtube.com/watch?v=youtube-video-id
---

# Transcript

Paste transcript text here.
```

## Summary Files

Summary files should be Markdown and use this format:

```markdown
---
videoId: youtube-video-id
title: Video title
url: https://www.youtube.com/watch?v=youtube-video-id
---

# Summary

Short summary of the full video.

## Key Topics

- Topic one
- Topic two

## Chapters

- `00:00` Chapter title
- `03:20` Chapter title

## Search Keywords

- keyword
- phrase people might search for
```

Draft summaries can be generated automatically by `scripts/ingest_video.py`. Hand-polished summaries are optional.
