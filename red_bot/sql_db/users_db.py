import logging


from red_bot.sql_db.bot_tables import Bot_tables_DB


class Users(Bot_tables_DB):

    '''
    Класс наследует основной класс :Bot_tables_DB:
    для реализации БД. Данный класс реализован с
    целью управления таблицей :users: по методу CRUD
    '''

    def __init__(self):
        super().__init__()

    def insert_users(
        self,
        user_id: int,
        user_phone: int,
        quantity_messages: int = 0
    ) -> None:
        self.cur.execute(
            '''
            INSERT INTO users (
                id,
                user_phone,
                quantity_messages
            )
            VALUES (?, ?, ?);            
            ''',
            (
                user_id,
                user_phone,
                quantity_messages
            )
        )
        self.conn.commit()
        logging.info(f'New user -- id: {user_id} has been added')

    def add_one_message(
        self,
        user_id: int
    ) -> None:
        self.cur.execute(
            '''
            UPDATE users
            SET quantity_messages = quantity_messages + 1
            WHERE id = ?
            ''',
            (user_id,)
        )
        self.conn.commit()

    def select_quantity_messages(
        self,
        user_id: int
    ) -> bool:
        self.cur.execute(
            '''
            SELECT quantity_messages FROM users
            WHERE id = ?
            ''',
            (user_id,)
        )
        return self.cur.fetchone()[0]

    def select_user(
        self,
        user_id: int
    ) -> tuple:
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
        user_id: int
    ) -> bool:
        self.cur.execute(
            '''
            SELECT COUNT(*) FROM users
            WHERE id = ?
            ''',
            (user_id,)
        )
        return self.cur.fetchone()[0]
    
    def select_all_data(self):
        self.cur.execute(
            '''
            SELECT * FROM users
            '''
        )
        return self.cur.fetchall()

    def delete_users(
        self,
        user_id: int
    ) -> None:
        self.cur.execute(
            '''
            DELETE FROM users
            WHERE id = ?
            ''',
            (user_id,)
        )
        self.conn.commit()
        logging.info(f'User {user_id} deleted')

    def erases_quantity_messages(self) -> None:
        self.cur.execute(
            '''
            UPDATE users
            SET quantity_messages = 0
            '''
        )
        self.conn.commit()