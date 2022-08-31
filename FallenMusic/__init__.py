import os
import time
import config
import asyncio

from os import listdir, mkdir
from rich.table import Table
from pyrogram import Client
from rich.console import Console as hehe
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as Bot

from FallenMusic.Helpers.Changers import *
from FallenMusic.Helpers.Clients import app, Ass
from FallenMusic.Helpers.Logging import startup_msg, startup_edit, startup_del


loop = asyncio.get_event_loop()
console = hehe()


## Startup Time
StartTime = time.time()

## Clients
app = app
Ass = Ass
aiohttpsession = ClientSession()

## Clients Info
BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""
ASSID = 0
ASSNAME = ""
ASSUSERNAME = ""
ASSMENTION = ""

## Config
OWNER_ID = config.OWNER_ID
F_OWNER = OWNER_ID[0]
LOGGER_ID = config.LOGGER_ID
SUDO_USERS = config.SUDO_USERS
MONGO_DB_URI = config.MONGO_DB_URI
DURATION_LIMIT = config.DURATION_LIMIT
DURATION_LIMIT_SEC = int(time_to_seconds(f"{config.DURATION_LIMIT}:00"))
ASS_HANDLER = config.ASS_HANDLER
PING_IMG = config.PING_IMG
START_IMG = config.START_IMG

## Modules
MOD_LOAD = []
MOD_NOLOAD = []

## MongoDB
MONGODB_CLI = Bot(config.MONGO_DB_URI)
db = MONGODB_CLI.Fallen


async def fallen_boot():
    global OWNER_ID, SUDO_USERS
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID, ASSNAME, ASSMENTION, ASSUSERNAME
    os.system("clear")
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(
        "\x46\x41\x4c\x4c\x45\x4e\x20\x4d\x55\x53\x49\x43\x20\x42\x4f\x54\x20\x3a\x20\x54\x48\x45\x20\x4d\x4f\x53\x54\x20\x41\x44\x56\x41\x4e\x43\x45\x44\x20\x4d\x55\x53\x49\x43\x20\x50\x4c\x41\x59\x45\x52\x20\x42\x4f\x54"
    )
    console.print(header)
    with console.status(
        "[magenta] Booting Fallen Music Bot...",
    ) as status:
        console.print("┌ [red]Booting Fallen Music Clients...\n")
        await app.start()
        await Ass.start()
        console.print("└ [green]Clients Booted Successfully!")
        initial = await startup_msg("**» ʙᴏᴏᴛɪɴɢ ғᴀʟʟᴇɴ ᴍᴜsɪᴄ ʙᴏᴛ...**")
        await asyncio.sleep(0.1)
        all_over = await startup_msg("**» ᴄʜᴇᴄᴋɪɴɢ ᴀɴᴅ ᴄʀᴇᴀᴛɪɴɢ ᴍɪssɪɴɢ ᴅɪʀᴇᴄᴛᴏʀɪᴇs...**")
        console.print(
            "\n┌ [red]Checking the existence of Required Directories..."
        )
        if "raw_files" not in listdir():
            mkdir("raw_files")
        if "downloads" not in listdir():
            mkdir("downloads")
        if "Cache" not in listdir():
            mkdir("Cache")
        console.print("└ [green]Directories Updated!")
        await asyncio.sleep(0.1)
        ___ = await startup_edit(all_over, "**» ɢᴇᴛᴛɪɴɢ ᴄʟɪᴇɴᴛs ɪɴғᴏ...**")
        console.print("\n┌ [red]Getting Clients Info...")
        getme = await app.get_me()
        getass = await Ass.get_me()
        BOT_ID = getme.id
        ASSID = getass.id
        if getme.last_name:
            BOT_NAME = getme.first_name + " " + getme.last_name
        else:
            BOT_NAME = getme.first_name
        BOT_USERNAME = getme.username
        ASSNAME = (
            f"{getass.first_name} {getass.last_name}"
            if getass.last_name
            else getass.first_name
        )
        ASSUSERNAME = getass.username
        ASSMENTION = getass.mention
        console.print("└ [green]Successfully Loaded Clients Information !")
        await asyncio.sleep(0.1)
        ____ok = await startup_edit(___, "**» ʟᴏᴀᴅɪɴɢ sᴜᴅᴏ ᴜsᴇʀs...**")
        console.print("\n┌ [red]Loading Sudo Users...")
        SUDO_USERS = (SUDO_USERS + OWNER_ID)
        await asyncio.sleep(1)
        console.print("└ [green]Loaded Sudo Users Successfully!\n")
        await startup_del(____ok)
        await startup_del(initial)


loop.run_until_complete(fallen_boot())


def init_db():
    global db_mem
    db_mem = {}


init_db()
