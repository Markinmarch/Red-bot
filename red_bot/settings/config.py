'''
Файл содержит основные настроечные данные приложения.
'''


import os

from dotenv import load_dotenv

load_dotenv(dotenv_path = 'red_bot/settings/config.env')

BOT_TOKEN = os.getenv('BOT_TOKEN', '')

ADMIN_ID = os.getenv('ADMIN_ID', '')

REDIS_HOST = os.getenv('REDIS_HOST', '')

REDIS_PORT = os.getenv('REDIS_PORT', '')

REDIS_BD = os.getenv('REDIS_DB', '')

DATA_PATH = 'red_bot/datas'

DB_NAME = 'main_database'

CHANNEL_ID = -1001916083546

BOT_ID = 6026823407

CHANNEL_URL = 'https://t.me/sevastopol_adjutor'

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

COUNT_LIMIT_POSTS = 3

PAUSE_CREATE_POSTS = 300 #пауза между созданием постов

DROP_TIME = '04:00'
