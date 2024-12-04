import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '1923471'))
API_HASH = environ.get('API_HASH', 'fcdc178451cd234e63faefd38895c991')
BOT_TOKEN = environ.get('BOT_TOKEN', "7814413831:AAGRr16DhSmAtxXM1XnIBCAKHBGlGArqQgs")

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '880087645').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/JAsuran2p0')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002396553917'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001188070894 -100169224324 -1002461730224 -1002223699552 -1002397109795 -1001775437494 -1001685364040 -1001274359769').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://mvideo:mvideo@cluster0.bpj54.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://mvideo:mvideo@cluster0.bpj54.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "asuranj1")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'AutofilterBot')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002396553917'))
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/Cps.jpg')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002396553917'))
URL = environ.get('URL', 'https://neutral-lynnet-dappa-159965a6.koyeb.app/')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002396553917'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/demoshort")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/demoshort")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/demoshort")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://envs.sh/Cpl.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "52d270ec96e971ba3c93464277f5c0393f053287")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "primeurl.in")
SHORTENER_API2 = environ.get("SHORTENER_API2", "")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "")
SHORTENER_API3 = environ.get("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "3600"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "21600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002316896807')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002133392581'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', False)
PM_SEARCH = is_enabled('PM_SEARCH', True)
