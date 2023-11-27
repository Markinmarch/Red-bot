import logging
import os
import sqlite3


from . import bot_tables
from . import posts_db
from . import responders_db
from . import users_db


from ..settings.config import DATA_PATH, DB_NAME



DB_tables = bot_tables.Bot_tables_DB(
    db_name = DB_NAME,
    db_path = DATA_PATH
)

def create_db() -> None:
    if DB_NAME + '.db' not in os.listdir(DATA_PATH):
        DB_tables.create_users_table()
        DB_tables.create_posts_table()
        DB_tables.create_responders_table()
    else:
        logging.info('--- Database for "SEVASTOPOL ADJUTOR BOT" connection established ---')

def start_db() -> None:
    try:
        create_db()
    except sqlite3.OperationalError:
        os.mkdir('red_bot/datas')
        create_db()

posts = posts_db.Posts()
users = users_db.Users()
responders = responders_db.Responders()
