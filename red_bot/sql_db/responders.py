import logging

from red_bot.sql_db.bot_tables import Bot_tables_DB
from red_bot.settings import config

class Responders(Bot_tables_DB):

    def __init__(
        self,
        name,
        path
    ):
        super().__init__(
            name = config.DB_NAME,
            path = config.DB_PATH
        )

    def insert_post(
        self,
        responder_id: int,
        post_id: int
    ):
        self.cur.execute(
            '''
            INSERT INTO responders (
                id,
                post_id
            )
            VALUES (?, ?);            
            ''',
            (
                responder_id,
                post_id,
            )
        )
        self.conn.commit()
        logging.info(f'User -- id: {responder_id} -- respond a post: {post_id}')

    def select_post(
        self,
        post_id: int
    ):
        self.cur.execute(
            '''
            SELECT id FROM responders
            WHERE post_id = (?);
            ''',
            (post_id)
        )
        return self.cur.fetchone()
