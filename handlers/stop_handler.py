from telegram import Update
from telegram.ext import CallbackContext
from utils.message_templates import stop_message

def stop(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(stop_message)
