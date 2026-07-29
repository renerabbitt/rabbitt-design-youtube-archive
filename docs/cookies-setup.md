# Export YouTube Cookies (VIP / Members-Only Access)

Chrome encrypts cookies, so the archive scripts cannot read your login directly.
Export a cookies file once, then VIP caption fetching works.

Save the file exactly here:

```text
C:\Users\rener\Dropbox\Assets\Workspaces\youtube repository\data\youtube.cookies.txt
```

Then tell the agent: **cookies ready**

---

## Step-by-step (Chrome)

### 1) Install the extension

1. Open Chrome.
2. Go to this page:  
   [Get cookies.txt LOCALLY](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
3. Click **Add to Chrome**.
4. Click **Add extension**.
5. If Chrome asks for permissions, click **Allow** / **Add extension**.

### 2) Pin the extension (so you can find it)

1. In Chrome’s toolbar, click the puzzle-piece icon (**Extensions**).
2. Find **Get cookies.txt LOCALLY**.
3. Click the pin icon so it stays visible on the toolbar.

### 3) Log into the correct YouTube account

1. Go to [https://www.youtube.com](https://www.youtube.com).
2. Make sure you are logged in as the **Rabbitt Design channel owner** account  
   (the same account that can open members-only / VIP videos and see **Edit video**).
3. Quick check: open your channel  
   [https://www.youtube.com/@rabbittdesign8482](https://www.youtube.com/@rabbittdesign8482)  
   and confirm you see **Customize channel** / **Manage videos**.
4. Also open one members-only video and confirm it plays (not a “Join this channel” wall).

### 4) Export cookies while still on YouTube

1. Stay on a `youtube.com` page (homepage or your channel is fine).
2. Click the **Get cookies.txt LOCALLY** toolbar icon.
3. In the popup:
   - Prefer **Export** / **Export as Netscape** / **Export for current site**
   - Do **not** choose JSON if both options appear
4. Chrome will download a file, usually named something like:
   - `cookies.txt`
   - `youtube.com_cookies.txt`
   - `www.youtube.com_cookies.txt`
5. That file normally lands in your **Downloads** folder:  
   `C:\Users\rener\Downloads\`

### 5) Move/rename the file into this project

1. Open File Explorer.
2. Go to Downloads and find the cookies file you just exported.
3. Copy it to:

```text
C:\Users\rener\Dropbox\Assets\Workspaces\youtube repository\data\
```

4. Rename it exactly to:

```text
youtube.cookies.txt
```

Final full path must be:

```text
C:\Users\rener\Dropbox\Assets\Workspaces\youtube repository\data\youtube.cookies.txt
```

### 6) Confirm the file looks right

1. Open `youtube.cookies.txt` in Notepad.
2. The first lines should look similar to:

```text
# Netscape HTTP Cookie File
...
.youtube.com	TRUE	/	TRUE	0	LOGIN_INFO	...
.youtube.com	TRUE	/	FALSE	0	SID	...
```

3. You should see `.youtube.com` somewhere in the file.
4. Close Notepad.
5. Reply in chat: **cookies ready**

---

## What happens next

The agent will run:

```powershell
py scripts/fetch_transcripts.py --pending --limit 20 --cookies data/youtube.cookies.txt
```

That uses your exported login to pull VIP/members-only captions into the archive.

---

## Security notes

- Treat `youtube.cookies.txt` like a password. Anyone with it can act as your logged-in YouTube session.
- It is gitignored and should not be committed.
- If VIP fetching suddenly fails later, export a fresh cookies file (logins expire).
