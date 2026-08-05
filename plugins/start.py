from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from core.clients import app
from config import (
    BOT_NAME,
    OWNER_USERNAME,
    SUPPORT_CHAT,
    UPDATES_CHANNEL,
)


@app.on_message(filters.command("start"))
async def start_command(client, message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ Add Me",
                    url=f"https://t.me/{client.me.username}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton("📚 Help", callback_data="help"),
                InlineKeyboardButton("📊 Stats", callback_data="stats"),
            ],
            [
                InlineKeyboardButton(
                    "📢 Updates",
                    url=f"https://t.me/{UPDATES_CHANNEL}",
                ),
                InlineKeyboardButton(
                    "💬 Support",
                    url=f"https://t.me/{SUPPORT_CHAT}",
                ),
            ],
            [
                InlineKeyboardButton(
                    "👨‍💻 Developer",
                    url=f"https://t.me/{OWNER_USERNAME}",
                )
            ],
        ]
    )

    text = f"""
✨ **Welcome to {BOT_NAME}**

🎵 Professional Telegram Music Bot

✅ High Quality Music
✅ Fast Streaming
✅ Queue System
✅ Admin Controls
✅ Modern UI

Click the buttons below to get started.
"""

    await message.reply_text(
        text,
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
