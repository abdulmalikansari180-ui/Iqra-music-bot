import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Bot Information
BOT_NAME = os.getenv("BOT_NAME", "Iqra Music")
BOT_USERNAME = os.getenv("BOT_USERNAME", "")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "")

# Database
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

# Pyrogram Session
STRING_SESSION = os.getenv("STRING_SESSION", "")

# Support
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "")

# Spotify
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

# YouTube
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")

# Logs
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))

# Images
START_IMAGE_URL = os.getenv("START_IMAGE_URL", "")
