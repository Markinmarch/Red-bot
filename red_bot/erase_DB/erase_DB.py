import logging
import redis
import threading


from red_bot.settings.config import REDIS_BD, REDIS_HOST, REDIS_PORT, DROP_TIME
from red_bot.sql_db.bot_tables import Bot_tables_DB



def erase_databases(self):
    # очищаем redis
    redis_db = redis.Redis(
        host = REDIS_HOST,
        port = REDIS_PORT,
        db = REDIS_BD,
    )
    redis_db.flushdb(asynchronous = True)
    # очищаем SQL
    Bot_tables_DB.drop_responders_table()
    Bot_tables_DB.drop_posts_table()

def timer_to_erase():
    timer = threading.Timer(
        interval = DROP_TIME,
        function = EraseDataBases.erase_databases()
    )
    timer.start()