import logging


from red_bot.sql_db.bot_tables import Bot_tables_DB
from red_bot.settings import config


class Users(Bot_tables_DB):

    def __init__(
            self,
            name,
            path
        ):
        super().__init__(
            name,
            path
        )


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
            '''
            SELECT * FROM users
            WHERE id = ?
            ''',
            (user_id,)
        )
        return self.cur.fetchone()

    def checking_users(
        self,
        user_id
    ):
        self.cur.execute(
            '''
            SELECT COUNT(*) FROM users
            WHERE id = ?
            ''',
            (user_id,)
        )
        return self.cur.fetchall()[0]

    def delete_users(
        self,
        user_id: int
    ):
        self.cur.execute(
            '''
            DELETE FROM users
            WHERE id = ?
            ''',
            (user_id,)
        )
        self.conn.commit()
        logging.info(f'User {user_id} deleted')

users = Users(
    name = config.DB_NAME,
    path = config.DB_PATH
)