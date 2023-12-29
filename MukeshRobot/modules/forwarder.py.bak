from telegram import Update

from MukeshRobot import telethn as tbot
from MukeshRobot.events import register

LOG_GROUP_ID = -1002014693954  # Replace with your log group ID

@register(pattern=".*")
async def forward_to_log_group(update: Update):
    # Check if the update is a message
    if update.message:
        log_group_id = LOG_GROUP_ID

        # Check if the message is from a private chat (DM)
        if update.message.chat.type == 'private':
            # Forward the message to the log group
            await update.message.forward(chat_id=log_group_id)
        elif hasattr(update.message.chat, 'type') and update.message.chat.type in ['group', 'supergroup']:
            # Handle group-specific logic here
            # For example, you might want to log information about the group message
            print("Received a message in a group:", update.message.text)
