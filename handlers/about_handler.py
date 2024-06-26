from telegram import Update
from telegram.ext import CallbackContext
from utils.message_templates import about_message

def about(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(about_message)
