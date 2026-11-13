import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Help", "About"], ["Ping", "Instagram"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome to InstaConnect!\n\n"
        "Your personal Telegram assistant for Instagram.\n"
        "Use the buttons below or type /help",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this message\n"
        "/about - About InstaConnect\n"
        "/ping - Check if bot is alive\n"
        "/profile - Look up an Instagram username\n"
        "/stories - Check stories (coming soon)\n\n"
        "Or just send a username and I’ll try to look it up."
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "InstaConnect Bot\n"
        "Manage Instagram from Telegram.\n"
        "Currently in early version — more features coming!"
    )

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pong! Bot is online ✅")

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        username = context.args[0].replace("@", "")
        await update.message.reply_text(f"Looking up Instagram profile: @{username}\n(Full lookup coming in next update)")
    else:
        await update.message.reply_text("Usage: /profile username")

async def stories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Stories feature is coming soon!")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text == "instagram":
        await update.message.reply_text(
            "Instagram tools:\n"
            "/profile username — Look up a profile\n"
            "/stories — Check stories (coming soon)\n\n"
            "Or just send a username."
        )
    elif text in ["help", "about", "ping"]:
        return
    else:
        await update.message.reply_text(f"You said: {update.message.text}\nTry /profile {update.message.text}")

def main():
    if not TOKEN:
        logger.error("BOT_TOKEN not set!")
        return
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("profile", profile))
    app.add_handler(CommandHandler("stories", stories))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    logger.info("Bot starting...")
    app.run_polling()

if __name__ == "__main__":
    main()