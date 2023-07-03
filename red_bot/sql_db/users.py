import logging


from red_bot.sql_db.bot_tables import Bot_main_DB


class Users(Bot_main_DB):

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
            f'''SELECT * FROM users
            WHERE id = {user_id};
            '''
        )
        return self.cur.fetchall()

    def ids_users(self):
        self.cur.execute(f'''SELECT id FROM users;''')
        return self.cur.fetchall()

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