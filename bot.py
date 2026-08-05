import logging
from pyrogram import idle

from core.clients import app
from core.loader import load_plugins

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] | %(levelname)s | %(name)s | %(message)s",
)

LOGGER = logging.getLogger("IqraMusic")


def main():
    LOGGER.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    LOGGER.info("🚀 Starting Iqra Music Bot")

    # Load Plugins
    load_plugins()
    LOGGER.info("✅ Plugins Loaded")

    # Start Bot
    app.start()
    me = app.get_me()

    LOGGER.info(f"🤖 Logged in as: {me.first_name}")
    LOGGER.info(f"🆔 Username: @{me.username}")
    LOGGER.info("✅ Bot Started Successfully")
    LOGGER.info("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    idle()

    LOGGER.info("🛑 Stopping Bot...")
    app.stop()


if __name__ == "__main__":
    main()
