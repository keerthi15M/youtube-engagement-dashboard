# -------------------------------------------------------
# YOUTUBE SHORTS ENGAGEMENT DASHBOARD (TOP 6) + CLEAN TITLES + GITHUB PUSH
# -------------------------------------------------------
from googleapiclient.discovery import build
import pandas as pd
import os
from git import Repo
import shutil
from isodate import parse_duration
import re

# -------------------------------------------------------
# 1. API Setup
# -------------------------------------------------------
API_KEY = "AIzaSyB1TQnZnklbORQ0inHUFTRYfq83TADLRHA"
CHANNEL_ID = "UCqgUt3T_tUGQ4ZTNo7RNFCg"

youtube = build("youtube", "v3", developerKey=API_KEY)

# -------------------------------------------------------
# 2. Get Uploads Playlist
# -------------------------------------------------------
def get_uploads_playlist(channel_id):
    res = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()
    return res["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

UPLOADS_PLAYLIST = get_uploads_playlist(CHANNEL_ID)

# -------------------------------------------------------
# 3. Get All Uploaded Video IDs
# -------------------------------------------------------
def get_video_ids(playlist_id):
    video_ids = []
    nextPageToken = None

    while True:
        res = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=nextPageToken
        ).execute()

        for item in res["items"]:
            video_ids.append(item["contentDetails"]["videoId"])

        nextPageToken = res.get("nextPageToken")
        if not nextPageToken:
            break

    return video_ids

video_ids = get_video_ids(UPLOADS_PLAYLIST)
print(f"Total uploaded videos found: {len(video_ids)}")

# -------------------------------------------------------
# 4. Clean Main Title Function
# -------------------------------------------------------
def clean_title(original_title):
    """
    Extracts the main title and removes:
    - hashtags (#shorts etc.)
    - emojis
    - extra words after separators like "|" or "-"
    
    Keeps ONLY the clean main title.
    """

    title = original_title

    # Remove anything after separators like | - :
    title = re.split(r"\||\-|:|–", title)[0]

    # Remove hashtags and emojis
    title = re.sub(r"#\S+", "", title)

    # Remove emojis using unicode ranges
    title = re.sub(r"[\U00010000-\U0010ffff]", "", title)

    # Remove multiple spaces
    title = re.sub(r"\s+", " ", title)

    return title.strip()

# -------------------------------------------------------
# 5. Get Shorts Metrics
# -------------------------------------------------------
def get_shorts_metrics(video_ids):
    shorts_data = []

    for i in range(0, len(video_ids), 50):
        res = youtube.videos().list(
            part="snippet,statistics,contentDetails",
            id=",".join(video_ids[i:i+50])
        ).execute()

        for video in res["items"]:
            snippet = video["snippet"]
            stats = video["statistics"]

            # Extract duration
            try:
                duration = parse_duration(video["contentDetails"]["duration"]).total_seconds()
            except:
                duration = None

            title_text = snippet["title"].lower()

            # ---- SHORTS DETECTION ----
            is_short = False
            if duration is not None and duration <= 60:
                is_short = True
            if "#short" in title_text or "#shorts" in title_text:
                is_short = True

            if not is_short:
                continue

            cleaned = clean_title(snippet["title"])

            shorts_data.append({
                "Title": cleaned,
                "Views": int(stats.get("viewCount", 0)),
                "Likes": int(stats.get("likeCount", 0)),
                "Comments": int(stats.get("commentCount", 0)),
                "Duration_sec": duration
            })

    return pd.DataFrame(shorts_data)

df_shorts = get_shorts_metrics(video_ids)
print(f"Total Shorts detected: {len(df_shorts)}")

# -------------------------------------------------------
# 6. TOP 6 SHORTS
# -------------------------------------------------------
df_top6 = df_shorts.sort_values("Views", ascending=False).head(6)
print("\nTOP 6 Shorts Clean Table:\n")
print(df_top6)

# -------------------------------------------------------
# 7. Save CSV
# -------------------------------------------------------
csv_file = "youtube_top6_clean.csv"
df_top6.to_csv(csv_file, index=False)
print(f"\nSaved CSV → {csv_file}")

# -------------------------------------------------------
# 8. PUSH TO GITHUB (WITH FIXED MAIN BRANCH)
# -------------------------------------------------------
GITHUB_REPO_URL = "https://github.com/keerthi15M/youtube-engagement-dashboard"
LOCAL_REPO_DIR = "youtube_dashboard_repo"

# Create folder
if not os.path.exists(LOCAL_REPO_DIR):
    os.makedirs(LOCAL_REPO_DIR)

# Copy CSV
shutil.copy(csv_file, LOCAL_REPO_DIR)

# Setup repo
if not os.path.exists(os.path.join(LOCAL_REPO_DIR, ".git")):
    repo = Repo.init(LOCAL_REPO_DIR)
    repo.create_remote("origin", GITHUB_REPO_URL)

    # Create main branch
    repo.git.checkout("-b", "main")
else:
    repo = Repo(LOCAL_REPO_DIR)

# Commit & push
repo.git.add(all=True)
repo.index.commit("Updated Top 6 YouTube Shorts Engagement CSV")

origin = repo.remotes.origin
origin.push(refspec="master:main")

print("\n✅ Successfully pushed to GitHub!")
