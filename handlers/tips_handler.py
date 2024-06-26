from telegram import Update
from telegram.ext import CallbackContext
from utils.message_templates import tips_message

def tips(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(tips_message)
