# Import libraries
import eel
from googleapiclient.discovery import build

# Initialize Eel
eel.init("web")

# Replace with your API key
DEVELOPER_KEY = "API_KEY_PLZ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Create YouTube API client
youtube = build(
    YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY
)

nextPageToken = None

# Expose functions to Javascript
@eel.expose
def search_videos(query, pageToken=None):
    global nextPageToken

    response = youtube.search().list(q=query,
        part="snippet",
        type="VIDEO",
        pageToken=pageToken,
        maxResults=50,
        order="relevance",
    ).execute()
    videos = response["items"]
    return videos

@eel.expose
def get_video_details(video_id):
    request = youtube.videos().list(
        id=video_id,
        part="snippet,contentDetails",
    )
    response = request.execute()
    return response["items"][0]

@eel.expose
def play_video(video_id):
    embed_url = f"https://www.youtube.com/embed/{video_id}"
    embed_html = f"<iframe width='560' height='315' src='{embed_url}' frameborder='0' allowfullscreen></iframe>"
    eel.set_video_source_and_play(embed_html)
    return embed_html

# Start Eel app
eel.start("index.html", mode="default")
