import logging
import redis


from sql_db.main import users


def erase_databases(
    host,
    port,
    db
) -> None:
    '''
    Метод очищает данные из Redis и заменяет* данные 
    одной из колонок в SQL базе данных
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
