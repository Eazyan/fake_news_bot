import os
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from handlers import start_handler, help_handler, about_handler, tips_handler, stop_handler

# TOKEN = os.getenv('7026865553:AAGdEondjiVC0k6blTvXmDt2DvJmZEvXq6c')

def main():
    # updater = Updater(TOKEN)
    updater = Updater('7026865553:AAGdEondjiVC0k6blTvXmDt2DvJmZEvXq6c')

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_handler.start))
    dispatcher.add_handler(CommandHandler('help', help_handler.help))
    dispatcher.add_handler(CommandHandler('about', about_handler.about))
    dispatcher.add_handler(CommandHandler('tips', tips_handler.tips))
    dispatcher.add_handler(CommandHandler('stop', stop_handler.stop))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

