from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI

mongo_client = AsyncIOMotorClient(MONGO_DB_URI)

db = mongo_client["IqraMusic"]

users_db = db["users"]
groups_db = db["groups"]
playlist_db = db["playlists"]
settings_db = db["settings"]
stats_db = db["stats"]
