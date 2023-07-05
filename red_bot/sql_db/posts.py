import logging


from red_bot.sql_db.bot_tables import Bot_tables_DB
from red_bot.settings import config

class Posts(Bot_tables_DB):

    def __init__(
        self,
        name,
        path
    ):
        super().__init__(
            name,
            path
        )

    def insert_post(
        self,
        post_id: int,
        user_id: int
    ):
        self.cur.execute(
            '''
            INSERT INTO posts (
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
            f'''SELECT user_id FROM posts
            WHERE id = {post_id};
            '''
        )
        return self.cur.fetchone()
    
    def select_posts(
        self,
        user_id: int
    ):
        self.cur.execute(
            f'''SELECT id FROM posts
            WHERE user_id = {user_id};
            '''
        )
        return self.cur.fetchall()
        
posts_db = Posts(
    name = config.DB_NAME,
    path = config.DB_PATH
)