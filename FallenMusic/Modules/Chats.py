from FallenMusic import app, OWNER_ID
from pyrogram import Client, filters
from pyrogram.types import Message
from FallenMusic.Helpers.Database import get_served_chats


@app.on_message(filters.command(["chats", "chatlist", "groups"]) & filters.user(OWNER_ID))
async def list_chats(_, message: Message):
    served_chats = []
    text = "🤯 **ʟɪsᴛ ᴏғ ᴄʜᴀᴛs ɪɴ ᴡʜɪᴄʜ ʙᴏᴛ ɪs ᴩʀᴇsᴇɴᴛ :**\n\n"
    try:
        chats = await get_served_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        await message.reply_text(f"ᴇʀʀᴏʀ : `{e}`")
        return
    count = 0
    for served_chat in served_chats:
        try:
            title = (await app.get_chat(served_chat)).title
        except Exception:
            title = "• ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        count += 1
        text += f"**• {count}. {title}** [`{served_chat}`]\n"
    if not text:
        await message.reply_text("**» ɴᴏ ᴄʜᴀᴛs ғᴏᴜɴᴅ ɪɴ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.**")  
    else:
        await message.reply_text(text) 

