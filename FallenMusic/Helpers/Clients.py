import config

from pyrogram import Client


app = Client(
    "FallenMusic",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)
Ass = Client(config.STRING_SESSION, config.API_ID, config.API_HASH)
