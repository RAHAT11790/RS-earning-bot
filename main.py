import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread

# ---------------- Config ----------------
BOT_TOKEN = os.getenv("8496840003:AAG88MWo80q4hYGFKoO0Jnz59qIo1sx5ZIY")

GROUP_URL = "https://t.me/hindianime03"
CHANNEL_URL = "https://t.me/cartoonfunny03"
EARNING_URL = "https://rsearnine02.blogspot.com/?m=1"   # WebApp লিংক

# ---------------- Logging ----------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("RS EARNING BOT")

# ---------------- Keyboards --------------
def home_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Group", url=GROUP_URL),
         InlineKeyboardButton("Channel", url=CHANNEL_URL)],
        [InlineKeyboardButton("💰 Start Earning", web_app=WebAppInfo(url=EARNING_URL))],
    ])

# ---------------- Handlers ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        f"হ্যালো {update.effective_user.first_name}! 👋\n\n"
        "🚀 স্বাগতম **RS EARNING BOT**-এ!\n\n"
        "শুধু অ্যাডস দেখেই আয় করুন।\n\n"
        "💿 Conversion Rate → 1000 Coins = 5৳\n\n"
        "বন্ধুদের আমন্ত্রণ করুন — আপনার রেফার কোড দিন ১০০ কয়েন জিতেনিন!"
    )
    await update.message.reply_text(text, reply_markup=home_keyboard(), parse_mode="Markdown")

# ---------------- Keep Alive (Flask) ----------------
app_flask = Flask('')

@app_flask.route('/')
def home():
    return "RS EARNING BOT is alive!"

def run():
    app_flask.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ---------------- Main ----------------
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    logger.info("RS EARNING BOT is running…")
    app.run_polling()

if __name__ == "__main__":
    keep_alive()  # Flask সার্ভার চালু (২৪/৭ active রাখবে)
    main()
