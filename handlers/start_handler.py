from telegram import Update
from telegram.ext import CallbackContext
from utils.message_templates import start_message

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(start_message)
