import logging
import redis


from sql_db.main import users
from red_bot.settings.config import REDIS_BD, REDIS_HOST, REDIS_PORT


def erase_databases() -> None:
    # очищаем redis
    redis_db = redis.Redis(
        host = REDIS_HOST,
        port = REDIS_PORT,
        db = REDIS_BD,
    )
    redis_db.flushdb(asynchronous = True)

    #обнуляем количество сообщений за пользователем в таблице пользователей
    users.erases_quantity_messages()
    logging.info('--- Databases erased ---')
