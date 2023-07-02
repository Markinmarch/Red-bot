import os
import logging
import sqlite3


from red_bot.settings import config
from red_bot.sql_db.users_db import Users


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