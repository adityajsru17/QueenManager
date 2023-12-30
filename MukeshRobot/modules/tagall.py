import asyncio
from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator
from MukeshRobot import telethn as client
from MukeshRobot.modules.sql import gm_sql, gn_sql

spam_chats = []

@client.on(events.NewMessage(pattern="^@tagall ?(.*)"))
@client.on(events.NewMessage(pattern="^@all ?(.*)"))
@client.on(events.NewMessage(pattern="^/tagall ?(.*)"))
@client.on(events.NewMessage(pattern="^@mention ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__Only admins can mention all!__")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("__Give me one argument!__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg is None:
            return await event.respond(
                "__I can't mention members for older messages! (Messages sent before I'm added to the group)__"
            )
    else:
        return await event.respond(
            "__Reply to a message or give me some text to mention others!__"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if chat_id not in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
        if usrnum == 15:
            if mode == "text_on_cmd":
                txt = f"{msg}\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(3)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if event.chat_id not in spam_chats:
        return await event.respond("There is no process going on.")
    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__Only admins can execute this command!__")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("Stopped mention.")

@client.on(events.NewMessage(pattern="^/gmtag ?(.*)"))
async def custom_mention(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__Only admins can use custom mentions!__")

    if not event.pattern_match.group(1):
        return await event.respond("__Provide a message for custom mention!__")

    message = event.pattern_match.group(1)
    gm_sql.add_chat(chat_id, message)
    return await event.respond("__Custom mention message set successfully!__")

@client.on(events.NewMessage(pattern="^/gntag ?(.*)"))
async def custom_mention(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__Only admins can use custom mentions!__")

    if not event.pattern_match.group(1):
        return await event.respond("__Provide a message for custom mention!__")

    message = event.pattern_match.group(1)
    gn_sql.add_chat(chat_id, message)
    return await event.respond("__Custom mention message set successfully!__")

__mod_name__ = "Tᴀɢᴀʟʟ"
__help__ = """
──「  ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs 」──

❍ /tagall or @all '(reply to message or add another message) - Mention all members in your group, without exception.'

❍ /gmtag '(set a custom message) - Tag all members with good morning messages.'

❍ /gntag '(set a custom message) - Mention all members with good night messages.'
"""
