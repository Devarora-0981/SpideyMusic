import config

from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)
from FallenMusic import BOT_USERNAME, F_OWNER


def start_pannel():
        buttons = [
            [
                InlineKeyboardButton(
                    text="🥺 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ 🥺", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❄ ʜᴇʟᴩ ❄", callback_data="fallen_help"
                ),
                InlineKeyboardButton(
                    text="🥀 ᴏᴡɴᴇʀ 🥀", user_id=F_OWNER
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=config.SUPPORT_CHAT
                ),
                InlineKeyboardButton(
                    text="💫 ᴄʜᴀɴɴᴇʟ 💫", url=config.SUPPORT_CHANNEL
                ),
            ],
            [
                InlineKeyboardButton(
                    text="☁ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 👀", url="https://te.legra.ph/file/27d69e48b1e6fe2cab8d0.mp4"
                )
            ],
        ]
        return buttons


def private_panel():
        buttons = [
            [
                InlineKeyboardButton(
                    text="🥺 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ 🥺", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🥀 ᴏᴡɴᴇʀ 🥀", user_id=F_OWNER
                ),
                InlineKeyboardButton(
                    text="❄ ʜᴇʟᴩ ❄", callback_data="fallen_help"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=config.SUPPORT_CHAT
                ),
                InlineKeyboardButton(
                    text="💫 ᴄʜᴀɴɴᴇʟ 💫", url=config.SUPPORT_CHANNEL
                ),
            ],
            [
                InlineKeyboardButton(
                    text="☁ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 👀", url="https://te.legra.ph/file/27d69e48b1e6fe2cab8d0.mp4"
                ),
            ],
        ]
        return buttons

