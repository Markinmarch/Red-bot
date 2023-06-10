import os
import logging
import sqlite3
from red_bot.settings import config


class Users:

    def __init__(
        self,
        name,
        path,
    ):
        self.name = name
        self.path = path
        self.conn = sqlite3.connect(f'{self.path}/{self.name}.db')
        self.cur = self.conn.cursor()

    def create_db(self):
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
        logging.info('Database "USERS" connection established')     

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
                user_phone,
            )
        )
        self.conn.commit()
        logging.info(f'New user -- id: {user_id} -- name: {user_name} -- has been added')

    def select_user(
        self,
        user_id: int
    ):
        self.cur.execute(
            f'''SELECT * FROM users
            WHERE id = {user_id};
            '''
        )
        return self.cur.fetchall()

    def ids_users(self):
        self.cur.execute(f'''SELECT id FROM users;''')
        return self.cur.fetchone()

    def delete_users(
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
        logging.info(f'User {user_id} deleted')


users_database = Users('users_data', config.DB_PATH)
if config.DB_NAME not in os.listdir(config.DB_PATH):
    users_database.create_db()
    logging.info(f'Database "USERS" created')


class Users_posts(Users):

    def __init__(
        self,
        name,
        path
    ):
        super().__init__(
            name,
            path
        )

    def create_db(self):
        self.conn
        self.cur.execute(
            '''
            CREATE TABLE if NOT EXISTS users_posts(
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL
            );            
            '''
        )
        self.conn.commit()
        logging.info('Database "USERS_POSTS" connection established')
    
    def insert_post(
        self,
        post_id: int,
        user_id: int
    ):
        self.cur.execute(
            '''
            INSERT INTO users_posts (
                id,
                user_id
            )
            VALUES (?, ?);            
            ''',
            (
                post_id,
                user_id,
            )
        )
        self.conn.commit()
        logging.info(f'User -- id: {user_id} -- created a post: {post_id}')

    def select_user(
        self,
        post_id: int
    ):
        self.cur.execute(
            f'''SELECT user_id FROM users_posts
            WHERE id = {post_id};
            '''
        )
        return self.cur.fetchone()
    
    def delete_post(
        self,
        post_id: int
    ):
        self.cur.execute(
            f'''
            DELETE FROM users_posts 
            WHERE id = {post_id};
            '''
        )
        self.conn.commit()
        logging.info(f'User {post_id} deleted')

posts_database = Users_posts('posts_data', config.DB_PATH)
if config.DB_NAME not in os.listdir(config.DB_PATH):
    posts_database.create_db()
    logging.info(f'Database "USERS_POSTS" created')