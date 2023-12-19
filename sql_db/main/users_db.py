import logging


from . bot_tables import Bot_tables_DB


class Users(Bot_tables_DB):
    '''
    Объект наследует основной класс :Bot_tables_DB:
    Данный класс реализован с целью управления таблицей
    :users: по методу CRUD
    '''
    def __init__(self):
        super().__init__()

    def insert_users(
        self,
        user_id: int,
        user_phone: int,
        quantity_messages: int = 0
    ) -> None:
        '''
        Метод добавляет нового пользователя при регистрации в таблицу users
        -------------------------------------------------------------------
        parametrs:
            :users_id: идентификатор пользователя
            :users_phone: номер телефона пользователя
            :quantity_messages: количество сообщений пользователя, по умолчания = 0
        '''
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
        '''
        Метод добавляет в колонку пользователя :quantity_messages: еденицу
        ------------------------------------------------------------------
        parametrs:
            :users_id: идентификатор пользователя
        '''
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
        '''
        Метод возвращает количество :quantity_messages: сообщений от пользователя на канале за день
        -------------------------------------------------------------------------------------------
        parametrs:
            :users_id: идентификатор пользователя
        '''
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
        '''
        Метод возвращает данные о пользователе по идентификатору пользователя
        ---------------------------------------------------------------------
        parametrs:
            :users_id: идентификатор пользователя
        '''
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
        '''
        Метод проверяет наличие пользователя в БД по идентификатору
        -----------------------------------------------------------
        parametrs:
            :users_id: идентификатор пользователя
        '''
        self.cur.execute(
            '''
            SELECT COUNT(*) FROM users
            WHERE id = ?
            ''',
            (user_id,)
        )
        return self.cur.fetchone()[0]
    
    def delete_users(
        self,
        user_id: int
    ) -> None:
        '''
        Метод удаляет пользователя из БД
        ---------------------------------
        parametrs:
            :users_id: идентификатор пользователя
        '''
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
        '''Метод обновляет колонку :quantity_messages: на ноль.'''
        self.cur.execute(
            '''
            UPDATE users
            SET quantity_messages = 0
            '''
        )
        self.conn.commit()