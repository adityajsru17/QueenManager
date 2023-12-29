from telegram import Update

from MukeshRobot import telethn as tbot
from MukeshRobot.events import register

LOG_CHANNEL_ID = -1002014693954  # Replace with your log channel ID

@register(pattern=".*")
async def forward_to_log_channel(update: Update):
    # Check if the update is a message
    if update.message:
        chat_id = update.message.chat_id
        log_channel_id = LOG_CHANNEL_ID

        # Check if the message is from a private chat
        if update.message.chat.type == 'private':
            # Forward the message to the log channel
            await update.message.forward(chat_id=log_channel_id)

        # If you want to handle other types of messages (e.g., stickers, photos), you can add more conditions here
      
