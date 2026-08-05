from pyrogram import filters
from pyrogram.types import Message

from core.clients import app


@app.on_message(filters.command("ping"))
async def ping(_, message: Message):
    await message.reply_text("🏓 Pong!\n\n✅ Iqra Music Bot is Working.")
