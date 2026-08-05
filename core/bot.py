import logging
from pyrogram import idle

from core.clients import app

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] - %(levelname)s - %(name)s - %(message)s",
)

LOGGER = logging.getLogger("IqraMusic")


def start_bot():
    LOGGER.info("🚀 Starting Iqra Music Bot...")
    app.start()
    LOGGER.info("✅ Bot Started Successfully!")
    idle()
    LOGGER.info("🛑 Stopping Bot...")
    app.stop()


if __name__ == "__main__":
    start_bot()
