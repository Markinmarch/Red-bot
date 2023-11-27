import os
import logging


from . import bot_tables
from . import posts_db
from . import responders_db
from . import users_db


from ..settings.config import DB_PATH, DB_NAME


DB_tables = bot_tables.Bot_tables_DB()

if DB_NAME + '.db' not in os.listdir(DB_PATH):
    DB_tables.create_users_table()
    DB_tables.create_posts_table()
    DB_tables.create_responders_table()
else:
    logging.info('--- Database for "SEVASTOPOL ADJUTOR BOT" connection established ---')

posts = posts_db.Posts()
users = users_db.Users()
responders = responders_db.Responders()