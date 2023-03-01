import os
import logging
import sqlite3
import asyncio
from hot_offer_bot.core import config


class Database:

    def __init__(
        self,
        name,
        path,
    ):
        self.name = name
        self.path = path
        self.conn = sqlite3.connect(f'{self.path}/{self.name}.db')
        self.cur = self.conn.cursor()
        logging.info("Database connection established")

    def create_db(self):
        self.conn
        logging.info("Database created")
        self.cur.execute(
            '''
            CREATE TABLE if NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                user_name TEXT NOT NULL,
                user_age INTEGER NOT NULL,
                user_gender INTEGER NOT NULL,
                user_phone INTEGER NOT NULL
            );
            '''
        )
        self.conn.commit()     
        logging.info('Table created')


    def insert_users(
        self,
        user_id: int,
        user_name: str,
        user_age: int,
        user_gender: int,
        user_phone: int
    ):
        self.cur.execute(
            '''
            INSERT INTO users (
                id,
                user_name,
                user_age,
                user_gender,
                user_phone
            )
            VALUES (?, ?, ?, ?, ?);            
            ''',
            (
                user_id,
                user_name,
                user_age,
                user_gender,
                user_phone
            )
        )
        self.conn.commit()
        logging.info(f'New user -- id: {user_id} -- name: {user_name} -- has been added')

    async def select_users(
        self,
        user_id: int
    ):
        self.cur.execute(
            f'''SELECT * FROM users
            WHERE id = {user_id};
            '''
        )
        self.conn.commit()

    async def delete_users(
        self,
        user_id: int
    ):
        self.cur.execute(
            f'''
            DELETE FROM users 
            WHERE id = {user_id};
            '''
        )
        self.conn.commit()
        logging.info(f"User {user_id} deleted")


database = Database(config.DB_NAME, config.DB_PATH)
database.create_db()

# async def add():
#     database.insert_users(user_id=1, user_name='Павлик', user_age=20, user_gender=1, user_phone=8978)
# asyncio.run(add())
