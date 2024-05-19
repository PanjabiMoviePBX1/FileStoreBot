import os

API_ID = int(os.environ.get("20841292", 0))
API_HASH = os.environ.get("58c4e84b9b2506684df6447d3e324dd9", None)
BOT_TOKEN = os.environ.get("6965297070:AAH26oGq2oy-7KBDE6_C-tG5q9MkhRSBcwk", None)
DB_CHANNEL_ID = os.environ.get("-1002019889699")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("6052303737"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
