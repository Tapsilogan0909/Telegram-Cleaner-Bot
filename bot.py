from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

# 🔴 Replace this with your actual bot token
BOT_TOKEN = "8537403389:AAELf0i2rr-fs_UCBkEPhEIv7Y2wgu0Z4V0"


async def delete_join_leave(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message is None:
        return

    # When someone joins
    if message.new_chat_members:
        try:
            await message.delete()
            print("Deleted join message")
        except Exception as e:
            print(e)
        return

    # When someone leaves
    if message.left_chat_member:
        try:
            await message.delete()
            print("Deleted leave message")
        except Exception as e:
            print(e)
        return


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    handler = MessageHandler(filters.ALL, delete_join_leave)
    app.add_handler(handler)

    print("Bot running… Press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
