import os
import logging
import sqlite3
import asyncio
from red_bot.settings import config


class SQLDatabase:

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


database = SQLDatabase(config.DB_NAME, config.DB_PATH)
if config.DB_NAME not in os.listdir(config.DB_PATH):
    database.create_db()