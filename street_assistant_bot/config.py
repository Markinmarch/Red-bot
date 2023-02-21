import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN', '')

ADMIN_ID = os.getenv('ADMIN_ID', '')

DB_NAME = os.getenv('DB_NAME', '')

REDIS_HOST = os.getenv('REDIS_HOST', '')

REDIS_PORT = os.getenv('REDIS_PORT', '')

REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)