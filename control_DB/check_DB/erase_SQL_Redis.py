import logging
import redis


from sql_db import users


def erase_databases(
    host: str,
    port: int,
    db: int
) -> None:
    '''
    Метод очищает данные из Redis и заменяет* данные 
    одной из колонок в SQL базе данных
    ------------------------------------------------
    parametrs:
        :host: хост БД Redis
        :port: порт БД Redis
        :db: номер таблицы БД Redis (по умолчанию 0)
        * условно в таблице users число постов от пользователя
        quantity_messages стирается, по факту заменяется у всех на 0
    '''
    # очищаем redis
    redis_db = redis.Redis(
        host = host,
        port = port,
        db = db,
    )
    redis_db.flushdb(asynchronous = True)

    #обнуляем количество сообщений за пользователем в таблице пользователей
    users.erases_quantity_messages()
    logging.info('--- Databases erased ---')
