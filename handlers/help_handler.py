from telegram import Update
from telegram.ext import CallbackContext
from utils.message_templates import help_message

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(help_message)
