# Inbox

Prefer auto-fetch over dropping files here:

```powershell
py scripts/fetch_transcripts.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
py scripts/fetch_transcripts.py --pending --limit 10
```

Merlin fallback after copying a transcript:

```powershell
py scripts/clipboard_to_inbox.py --url "https://www.youtube.com/live/VIDEO_ID" --ingest
```

Or drop one file per video here, then run:

```powershell
py scripts/ingest_video.py --process-inbox
```

## File format

```text
Title: Template Tuesdays - Example Title
URL: https://www.youtube.com/live/VIDEO_ID
Visibility: members-only

0:00 Transcript starts here...
0:05 More transcript text...
```

Short form also works:

```text
Template Tuesdays - Example Title
https://www.youtube.com/live/VIDEO_ID

0:00 Transcript starts here...
```

Processed files move to `data/inbox/processed/`.
