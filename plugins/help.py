from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from core.clients import app


@app.on_message(filters.command("help"))
async def help_command(client, message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🎵 Play", callback_data="play_help"),
                InlineKeyboardButton("⏯ Queue", callback_data="queue_help"),
            ],
            [
                InlineKeyboardButton("⚙ Settings", callback_data="settings_help"),
                InlineKeyboardButton("👮 Admin", callback_data="admin_help"),
            ],
            [
                InlineKeyboardButton("🔙 Back", callback_data="home"),
            ],
        ]
    )

    text = """
📚 **Iqra Music Help Menu**

Choose a category below.

🎵 Music Commands
👮 Admin Commands
⚙ Settings
📜 Queue Commands

More features will be added automatically as the bot grows.
"""

    await message.reply_text(
        text,
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
