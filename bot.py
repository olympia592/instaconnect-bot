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