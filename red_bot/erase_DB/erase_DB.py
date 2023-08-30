import logging
import redis


from red_bot.settings.config import REDIS_BD, REDIS_HOST, REDIS_PORT
from red_bot.sql_db.posts_db import posts
from red_bot.sql_db.responders_db import responders



def erase_databases() -> None:
    # очищаем redis
    redis_db = redis.Redis(
        host = REDIS_HOST,
        port = REDIS_PORT,
        db = REDIS_BD,
    )
    redis_db.flushdb(asynchronous = True)
    # очищаем SQL
    responders.drop_responders_table()
    posts.drop_posts_table()
    
    logging.info('--- Databases erased ---')

