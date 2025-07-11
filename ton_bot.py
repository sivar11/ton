from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "ضع التوكن هنا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("افتح TON WebApp", web_app={"url": "https://ton-webapp.vercel.app"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("مرحبًا! اضغط لفتح التطبيق:", reply_markup=reply_markup)

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
