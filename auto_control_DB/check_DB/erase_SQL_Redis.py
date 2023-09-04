import logging
import redis
import time


from red_bot.sql_db.posts_db import posts
from red_bot.sql_db.responders_db import responders
from red_bot.settings.config import REDIS_BD, REDIS_HOST, REDIS_PORT, DROP_TIME


def erase_databases() -> None:
    # очищаем redis
    redis_db = redis.Redis(
        host = REDIS_HOST,
        port = REDIS_PORT,
        db = REDIS_BD,
    )
    redis_db.flushdb(asynchronous = True)
    # очищаем SQL
    responders.delete_responders_table()
    posts.delete_posts_table()
    logging.info('--- Databases erased ---')
