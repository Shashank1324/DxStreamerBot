import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = environ.get('API_ID',"11760418") 
    API_HASH = environ.get('API_HASH',"1087bd9fc871216be0e86287e5c50ac3") 
    BOT_TOKEN = environ.get('BOT_TOKEN',"6463692735:AAEGPGQuP4tIUwJ7FSBay8Y52wCW9MUFpU8")
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1904953726").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = environ.get('OWNER_USERNAME',"Uuuuiioopg")
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
       # URL = "https://{}/".format(FQDN)
       URL = FQDN
    else:
        #URL = "https://{}/".format(FQDN)
        URL = FQDN 
    DATABASE_URL = environ.get('DATABASE_URL',"mongodb+srv://Shashanklssss:shashank.ls1324@cluster0.ctzkp4x.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
