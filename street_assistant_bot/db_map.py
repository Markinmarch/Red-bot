import os
import logging
import sqlite3
import redis
import ujson

import config


# класс наследуется от redis.StrictRedis
class Cache(redis.StrictRedis):
    def __init__(self, host, port, password,
                 charset="utf-8",
                 decode_responses=True):
        super(Cache, self).__init__(host, port,
                                    password=password,
                                    charset=charset,
                                    decode_responses=decode_responses)
        logging.info("Redis start")

    def jset(self, name, value, ex=0):
        """функция конвертирует python-объект в Json и сохранит"""
        request = self.get(name)
        if request is None:
            return request
        return ujson.loads(request)

    def jget(self, name):
        """функция возвращает Json и конвертирует в python-объект"""
        return ujson.loads(self.get(name))


class Database:
    """ Класс работы с базой данных """
    def __init__(self, name):
        self.name = name
        self._conn = self.connection()
        logging.info("Database connection established")

    def create_db(self):
        connection = sqlite3.connect(f"{self.name}.db")
        logging.info("Database created")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE users 
                          (id INTEGER PRIMARY KEY,
                           leagues VARCHAR NOT NULL);''')
        connection.commit()
        cursor.close()

    def connection(self):
        db_path = os.path.join(os.getcwd(), f"{self.name}.db")
        if not os.path.exists(db_path):
            self.create_db()
        return sqlite3.connect(f"{self.name}.db")

    def _execute_query(self, query, select=False):
        cursor = self._conn.cursor()
        cursor.execute(query)
        if select:
            records = cursor.fetchone()
            cursor.close()
            return records
        else:
            self._conn.commit()
        cursor.close()

    async def insert_users(
        self,
        user_id: int,
        user_name: str,
        user_age: int,
        user_gender: str,
        user_phone: int
    ):
        insert_query = f'''
                        INSERT INTO users (
                            id,
                            user_name,
                            user_age,
                            user_gender,
                            user_phone
                        )
                        VALUES (
                            {user_id},
                            {user_name},
                            {user_age},
                            {user_gender},
                            {user_phone}
                        )
                        '''
    async def insert_users(self, user_id: int, leagues: str):
        insert_query = f"""INSERT INTO users (id, leagues)
                                       VALUES ({user_id}, "{leagues}")"""
        self._execute_query(insert_query)
        logging.info(f"Leagues for user {user_id} added")

    async def select_users(self, user_id: int):
        select_query = f"""SELECT leagues from leagues 
                           where id = {user_id}"""
        record = self._execute_query(select_query, select=True)
        return record

    async def update_users(self, user_id: int, leagues: str):
        update_query = f"""Update leagues 
                              set leagues = "{leagues}" where id = {user_id}"""
        self._execute_query(update_query)
        logging.info(f"Leagues for user {user_id} updated")

    async def delete_users(self, user_id: int):
        delete_query = f"""DELETE FROM users WHERE id = {user_id}"""
        self._execute_query(delete_query)
        logging.info(f"User {user_id} deleted")


# создание объектов cache и database
# cache = Cache(
#     host=config.REDIS_HOST,
#     port=config.REDIS_PORT,
#     password=config.REDIS_PASSWORD
# )
# database = Database(config.BOT_DB_NAME)