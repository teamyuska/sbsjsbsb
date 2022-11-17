from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["asistan"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Məni əvvəlcə admim etməlisiniz</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "SOA Asisstant"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
        return
    
@USER.on_message(filters.group & filters.command(["ayril", "asistanby"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>İstifadəçi qrupunuzdan ayrılamadı!."
            "\n\nYada özün çıxara bilərsən</b>",
        )
        return
 
 
 
