# webapp_bot.py
import os, json, logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN") or "8525604659:AAH-x1CGGWW8_pt9Aybv9h-iQgWhAjl095w"
WEBAPP_URL = "https://auroreine-miniapp.vercel.app/"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Open Profile Mini App ✨", web_app=WebAppInfo(url=WEBAPP_URL))]
    ])
    await update.message.reply_text("Tap tombol di bawah untuk membuka mini app:", reply_markup=keyboard)

async def webapp_data_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg or not msg.web_app_data:
        return
    raw = msg.web_app_data.data
    try:
        data = json.loads(raw)
    except:
        await msg.reply_text(f"Got raw data: `{raw}`", parse_mode="Markdown")
        return
    # contoh handling
    if data.get("type") == "profile_choice":
        who = data.get("value")
        if who == "zhou":
            await msg.reply_text("Kamu memilih ✦ Zhou Xinyu — nanti bot bisa kirim foto & lagu.")
        elif who == "rp":
            await msg.reply_text("Kamu memilih ✧ RP muse — nanti bot bisa kirim biodata RP.")
        else:
            await msg.reply_text(f"Kamu memilih: {who}")
    else:
        await msg.reply_text(f"Data mini-app: `{data}`", parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, webapp_data_handler))
    print("WebApp bot running. Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
