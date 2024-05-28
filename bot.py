from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen

bot = Client(
    "mo",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    royal = "Ux_Uv"
    # تأكد من استبدال 'chat_id' بمعرف الدردشة الصحيح
    await bot.send_message(chat_id=royal, text="**تم تشغيل الصانع عزيزي المطور ،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور🔮.")
    await idle()
