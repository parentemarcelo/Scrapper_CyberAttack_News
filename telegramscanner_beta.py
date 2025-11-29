########## Non working code #############
# To be reviewed and debugged


from telegram.ext import Updater, MessageHandler, Filters

# Your bot token from BotFather
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# List of keywords to search for in messages
keywords = ['keyword']

# Chat ID of the target group
TARGET_CHAT_ID = -123123123  # Replace with desired group chat ID

def message_handler(update, context):
    if update.message.chat_id == TARGET_CHAT_ID:
        message_text = update.message.text
        if any(keyword.lower() in message_text.lower() for keyword in keywords):
            print(f"Keyword found in message: {message_text}")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text & ~Filters.command, message_handler)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()