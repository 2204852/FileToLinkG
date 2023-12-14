from os import environ as env
from dotenv import load_dotenv
load_dotenv()


    
class Telegram:
    API_ID = int(env.get("API_ID", "27384907"))
    API_HASH = str(env.get("API_HASH", "141c715ecc46b78dbd15d34f83e259cb"))
    BOT_TOKEN = str(env.get("BOT_TOKEN",  "6976618488:AAH1e1F_KfkIH9VmJSljjeSV4eJXIGn98Ls"))
    OWNER_ID = int(env.get('OWNER_ID', '6177970139'))
    WORKERS = int(env.get("WORKERS", "10"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL', 'mongodb+srv://sowenb:HjeaAOK25jvuv1WF@cluster0.0tog2ts.mongodb.net/?retryWrites=true&w=majority' ))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "GKBOTZ"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_UPDATES_CHANNEL = env.get('FORCE_UPDATES_CHANNEL', "GKBOTZ")
    FORCE_UPDATES_CHANNEL = True
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    IMAGE_FILEID = env.get("IMAGE_FILEID", "https://telegra.ph/file/ea80f7cdbc7a9bfd9378c.jpg")
    MULTI_CLIENT = True
    LOG_CHANNEL = int(
        env.get("BIN_CHANNEL", "-1002116396818")
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))
class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "https://file-to-linkg-de135aadd914.herokuapp.com/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )
    KEEP_ALIVE = str(env.get("KEEP_ALIVE", "t").lower()) in ("1", "true", "t", "yes", "y")


