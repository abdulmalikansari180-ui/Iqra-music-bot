from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "IqraMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def alive(_, message):
    if message.text == "/alive":
        await message.reply_text("✅ Iqra Music Bot is Online!")

if __name__ == "__main__":
    print("🚀 Starting Iqra Music Bot...")
    app.run()
