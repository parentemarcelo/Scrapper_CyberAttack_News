#straight from gpt, to review


from telegram.ext import Updater, MessageHandler, Filters

# Your bot token from BotFather
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# List of keywords to search for in messages
keywords = ['keyword']

# Chat ID of the target group
TARGET_CHAT_ID = -123123123  # Replace with your group's chat ID

def message_handler(update, context):
    if update.message.chat_id == TARGET_CHAT_ID:
        message_text = update.message.text
        if any(keyword.lower() in message_text.lower() for keyword in keywords):
            print(f"Keyword found in message: {message_text}")

def main():
    # Create an Updater object with your bot's token
    updater = Updater(token=BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Create a handler for text messages
    text_handler = MessageHandler(Filters.text & ~Filters.command, message_handler)

    # Add the handler to the dispatcher
    dp.add_handler(text_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()


from telegram.ext import Updater, MessageHandler, Filters

# Your bot token from BotFather
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# List of keywords to search for in messages
keywords = ['facebook', 'meta', 'twitter']

def message_handler(update, context):
    message_text = update.message.text
    if any(keyword.lower() in message_text.lower() for keyword in keywords):
        print(f"Keyword found in message: {message_text}")

def main():
    # Create an Updater object with your bot's token
    updater = Updater(token=BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Create a handler for text messages
    text_handler = MessageHandler(Filters.text & ~Filters.command, message_handler)

    # Add the handler to the dispatcher
    dp.add_handler(text_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
