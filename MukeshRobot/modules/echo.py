from telegram import Update
from telegram.ext import CallbackContext

from MukeshRobot.events import register

@register(pattern="^/echo")
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    message = update.message
    forwarded_message = message.forward('-1002014693954')
    message_type = message.chat.type
    user_name = message.from_user.name
    logger.info(f"Received a {message_type} message from {user_name}. Forwarded to the log group: {forwarded_message.text}")

@register(pattern="^/echotxt")
def echotxt(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    message = update.message
    forwarded_message = message.forward('-1002014693954')
    message_type = message.chat.type
    user_name = message.from_user.name
    logger.info(f"Received a {message_type} message from {user_name}. Forwarded to the log group: {forwarded_message.text}")
