import config
from .Clients import app, Ass

failure = "Make sure your bot is in your log channel and is promoted as an admin with full rights !"


async def startup_msg(_message_):
    try:
        fallenwtf = await app.send_message(
            config.LOGGER_ID, f"{_message_}"
        )
        return fallenwtf
    except:
        print(failure)
        return


async def startup_edit(_message_id, _message_):
    try:
        fallenwtf = await app.edit_message_text(
            config.LOGGER_ID, _message_id.message_id, f"{_message_}"
        )
        return fallenwtf
    except:
        fallenwtf = await startup_send_new(_message_)
        return fallenwtf


async def startup_del(_message_id):
    try:
        await app.delete_messages(config.LOGGER_ID, _message_id.message_id)
        return bool(1)
    except:
        pass
