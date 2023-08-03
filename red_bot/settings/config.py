'''
Файл содержит основные настроечные данные приложения.
'''


import os

from dotenv import load_dotenv

load_dotenv(dotenv_path = 'red_bot/settings/config.env')

BOT_TOKEN = os.getenv('BOT_TOKEN', '')

ADMIN_ID = os.getenv('ADMIN_ID', '')

SQL_DB_NAME = os.getenv('DB_NAME', '')

REDIS_HOST = os.getenv('REDIS_HOST', '')

REDIS_PORT = os.getenv('REDIS_PORT', '')

REDIS_BD = os.getenv('REDIS_DB', '')

DB_NAME = os.getenv('DB_NAME', '')

DB_PATH = os.getenv('DB_PATH', '')

CHANNEL_ID = os.getenv('CHANNEL_ID', '')

BOT_ID = os.getenv('BOT_ID', '')

CHANNEL_URL = os.getenv('CHANNEL_URL', '')

BOT_URL = os.getenv('BOT_URL', '')

TIMEOUT_MESSAGES = {
    'registration': {
        'name': 20,
        'age': 20,
        'gender': 10,
        'phone': 10
    },
    'create_post': {
        'direction': 15,
        'title': 30,
        'text': 120,
        'conditions': 40,
        'photo': 30
    }
}

COUNT_LIMIT_POSTS = 3

PAUSE_CREATE_POSTS = 300 #пауза между созданием постов