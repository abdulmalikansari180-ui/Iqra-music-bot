import os

# Telegram API
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# MongoDB
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

# Bot Information
BOT_NAME = os.getenv("BOT_NAME", "Iqra Music")
BOT_USERNAME = os.getenv("BOT_USERNAME", "")
OWNER_NAME = os.getenv("OWNER_NAME", "Abdul Malik")
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "")

# Optional
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))
SUDO_USERS = list(
    map(int, os.getenv("SUDO_USERS", "").split()))
    if os.getenv("SUDO_USERS")
    else []
)
