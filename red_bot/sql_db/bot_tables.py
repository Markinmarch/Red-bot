import os
import logging
import sqlite3


from red_bot.settings import config


class Bot_tables_DB:
    '''
    Класс реализует создание связанных между собой таблиц базы данных.
        :name: параметр наименования базы данных
        :path: параметр маршрута до папки с базой данных
        :conn: параметр реализует подключение к сессии БД
        :cur: параметр указателя БД
    '''
    def __init__(
        self,
        name: str,
        path: str
    ):
        self.name = name
        self.path = path
        self.conn = sqlite3.connect(f'{self.path}/{self.name}.db')
        self.cur = self.conn.cursor()

    def create_users_tables(self):
        self.conn
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
        logging.info('--- Table "USERS" connection established ---')

    def create_posts_tables(self):
        self.conn
        self.cur.execute(
            '''
            CREATE TABLE if NOT EXISTS posts(
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );            
            '''
        )
        self.conn.commit()
        logging.info('--- Table "USERS_POSTS" connection established ---')

    def create_responders_tables(self):
        self.conn
        self.cur.execute(
            '''
            CREATE TABLE if NOT EXISTS responders(
                id INTEGER PRIMARY KEY,
                post_id INTEGER NOT NULL,
                FOREIGN KEY (post_id) REFERENCES posts(id)
            );            
            '''
        )
        self.conn.commit()
        logging.info('--- Table "RESPONDERS" connection established ---')


def create_table() -> None:
    if config.DB_NAME not in os.listdir(config.DB_PATH):
        DB_tables = Bot_tables_DB(config.DB_NAME, config.DB_PATH)
        DB_tables.create_users_tables()
        DB_tables.create_posts_tables()
        DB_tables.create_responders_tables()
        logging.info('--- Database for "SEVASTOPOL ADJUTOR BOT" has been created ---')

create_table()
