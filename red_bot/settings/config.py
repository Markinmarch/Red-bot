'''
Файл содержит основные данные для стабильной работы приложения.
'''


import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN', '')

ADMIN_ID = os.getenv('ADMIN_ID', '')

SQL_DB_NAME = os.getenv('DB_NAME', '')

REDIS_HOST = os.getenv('REDIS_HOST', '')

REDIS_PORT = os.getenv('REDIS_PORT', '')

REDIS_BD = os.getenv('REDIS_DB', '')

# REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')

# URL_PARSER = 'https://www.interpol.int/How-we-work/Notices/View-Red-Notices'