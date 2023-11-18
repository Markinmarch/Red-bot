'''
Файл содержит основные настроечные данные приложения.
'''


import os

from dotenv import load_dotenv

load_dotenv(dotenv_path = 'red_bot/settings/config.env')

BOT_TOKEN = os.getenv('BOT_TOKEN', '')

ADMIN_ID = 805875522

REDIS_HOST = 'localhost'

REDIS_PORT = 6379

REDIS_BD = 1

DATA_PATH = 'red_bot/datas'

DB_NAME = 'main_database'

CHANNEL_ID = -1001916083546

BOT_ID = 6026823407

CHANNEL_URL = 'https://t.me/sevastopol_assistant'

BOT_URL = 'https://t.me/street_assistant_bot'

TIMEOUT_MESSAGES = {
    'registration': {
        'name': 40,
        'age': 20,
        'gender': 10,
        'phone': 10
    },
    'create_post': {
        'direction': 40,
        'title': 60,
        'text': 600,
        'conditions': 300,
        'photo': 120
    },
    'delete_post': 60
}

COUNT_LIMIT_POSTS = 2

PAUSE_CREATE_POSTS = 300 #пауза между созданием постов

DROP_TIME = '04:00'

HOUR = 3600
