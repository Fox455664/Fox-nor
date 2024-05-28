from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen

# إنشاء عميل بوت
bot = Client(
    "mo",  # اسم الجلسة
    api_id=API_ID,  # معرف API
    api_hash=API_HASH,  # هاش API
    bot_token=BOT_TOKEN,  # رمز البوت
    plugins=dict(root="Maker")  # المسار إلى الإضافات
)

# تعريف وظيفة بدء البوت
async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")  # طباعة رسالة بدء البوت
    await bot.start()  # بدء البوت
    # استبدل '@F_o_x_5' بمعرف الدردشة الخاص بك
    await bot.send_message('@F_o_x_5', "**تم تشغيل الصانع عزيزي المطور،**")
    print("[INFO]: تم تشغيل الصانع وإرسال رسالة للمطور🔮.")  # طباعة رسالة تأكيد
    await idle()  # الانتظار للأحداث

# بعد تحديث الكود، إذا استمرت في تلقي هذا الخطأ:
# 2024-05-28T19:19:08.611152+00:00 app[worker.2]:     raise BadMsgNotification(result.error_code)
# 2024-05-28T19:19:08.611167+00:00 app[worker.2]: pyrogram.errors.BadMsgNotification: [16] The msg_id is too low, the client time has to be synchronized.
# 2024-05-28T19:19:08.769354+00:00 heroku[worker.2]: State changed from up to crashed
