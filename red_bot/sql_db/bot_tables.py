import logging
import sqlite3
import os


from ..settings.config import DB_PATH, DB_NAME


class Bot_tables_DB:
    '''
    Класс реализует создание связанных между собой таблиц базы данных.
        :name: параметр наименования базы данных
        :path: параметр маршрута до папки с базой данных
        :conn: параметр реализует подключение к сессии БД
        :cur: параметр указателя БД
    '''
    def __init__(self):
        self.name = DB_NAME
        self.path = DB_PATH
        self.conn = sqlite3.connect(f'{self.path}/{self.name}.db')
        self.cur = self.conn.cursor()

    def create_users_table(self) -> None:
        self.conn
        self.cur.execute(
            '''
            CREATE TABLE if NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                user_phone INTEGER NOT NULL,
                quantity_messages INTEGER NOT NULL
            );
            '''
        )
        self.conn.commit()
        logging.info('--- Table "USERS" has been created ---')

    def create_posts_table(self) -> None:
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
        logging.info('--- Table "POSTS" has been created ---')

    def drop_posts_table(self) -> None:
        self.cur.execute(
            '''
            DROP TABLE posts;
            '''
        )
        self.conn.commit()

    def create_responders_table(self) -> None:
        self.conn
        self.cur.execute(
            '''
            CREATE TABLE if NOT EXISTS responders(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                responder_id INTEGER NOT NULL,
                post_id INTEGER NOT NULL,
                FOREIGN KEY (post_id) REFERENCES posts(id)
            );            
            '''
        )
        self.conn.commit()
        logging.info('--- Table "RESPONDERS" has been created ---')

def create_db() -> None:
    if DB_NAME + '.db' not in os.listdir(DB_PATH):
        Bot_tables_DB().create_users_table()
        Bot_tables_DB().create_posts_table()
        Bot_tables_DB().create_responders_table()
    else:
        logging.info('--- Database for "SEVASTOPOL ADJUTOR BOT" connection established ---')

def start_db() -> None:
    try:
        create_db()
    except FileNotFoundError:
        os.mkdir('red_bot/datas')
        create_db()

