import logging, sqlite3, os


from . import DB_PATH, DB_NAME


class Bot_tables_DB:
    '''
    Класс реализует создание связанных между собой таблиц базы данных.
    ------------------------------------------------------------------
    parametrs:
        :conn: параметр реализует подключение к сессии БД
        :cur: параметр указателя БД
    '''
    def __init__(self):
        self.conn = sqlite3.connect(f'{DB_PATH}/{DB_NAME}.db')
        self.cur = self.conn.cursor()

    def create_users_table(self) -> None:
        '''Метод создаёт таблицу users'''
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
        '''Метод создаёт таблицу posts'''
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

    def create_responders_table(self) -> None:
        '''Метод создаёт таблицу responders'''
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
    '''Метод проверяет наличие БД в директории, при отсутствии создаёт таблицы'''
    if DB_NAME + '.db' not in os.listdir(DB_PATH):
        Bot_tables_DB().create_users_table()
        Bot_tables_DB().create_posts_table()
        Bot_tables_DB().create_responders_table()
    else:
        logging.info('--- Database for "SEVASTOPOL ADJUTOR BOT" connection established ---')

def start_db() -> None:
    '''Метод проверяет наличие директории, при отсутствии создаёт её'''
    try:
        create_db()
    except FileNotFoundError:
        os.mkdir(DB_PATH)
        create_db()