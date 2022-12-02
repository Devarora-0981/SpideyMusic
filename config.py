from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "17605524"))
API_HASH = getenv("API_HASH", "94e442949fc57d21e0a6212a7e600483")

ASS_HANDLER = list(getenv("ASS_HANDLER", "/").split())
BOT_TOKEN = getenv("BOT_TOKEN", "5660006605:AAEi0Fp3W87o7kz1wllqoZrxfH_tnWuWDyc")


DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001856067789"))
MONGO_DB_URI = getenv("MONGO_DB_URI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1697845783").split()))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/8021f124a9a418cb61a98.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/eec6dcc33de8add5ad2f0.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/The_Royal_Squad21")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/uknowrohit")

STRING_SESSION = getenv("STRING_SESSION", "BQCFBsdrTDVAFyEUANlmGu_tPLDNEeQmfci2rezmo9-AAmO4SOHGP9monQGIXKAcrh6mkTrUgcHZ-PRkQY8mVRzTpyKyFa0K6aw0RGmuKPBKoOu5ujQFiiX2rrnDx4ykKA-B_buDjbliWXV7rhRWkoqk7UMfZgZRP8bG_dv7S1ZOyGszl3KMG6klBEfkUaTGJg9iHcEnxRlQ8FJDRqeVt7UmoSPl9vV0oT8JaPeo3v0w6BSDwNplaUksNvOnz1uFy2C1-E5fRK4xtwuRNtpQAn1ry8XeQ4dcEreY0STWsnTi0QHHj3T3xUWT84oCsH7W0pHN8fjYI-3t_JXLRGN2pM0FbqGMlQA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1697845783").split()))
