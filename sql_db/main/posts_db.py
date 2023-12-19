import logging


from . bot_tables import Bot_tables_DB


class Posts(Bot_tables_DB):
    '''
    Объект наследует основной класс :Bot_tables_DB:
    Данный класс реализован с целью управления таблицей
    :posts: по методу CRUD
    '''
    def __init__(self):
        super().__init__()

    def insert_post(
        self,
        post_id: int,
        user_id: int
    ):
        '''
        Метод добавляет пост от пользователя
        -------------------------------------
        parametrs:
            :post_id: идентификатор поста
            :user_id: идентификатор пользователя
        '''
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
                user_id
            )
        )
        self.conn.commit()
        logging.info(f'User -- id: {user_id} -- created a post: {post_id}')

    def select_user(
        self,
        post_id: int
    ):
        '''
        Метод получает идентификатор пользователя по индикатору поста
        -------------------------------------------------------------
        parametrs:
            :post_id: идентификатор поста
        '''
        self.cur.execute(
            '''
            SELECT user_id FROM posts
            WHERE id = (?)
            ''',
            (post_id,)
        )
        return self.cur.fetchone()
   
    def select_posts(
        self,
        user_id: int
    ):
        '''
        Метод получает идентификатор постов по идентификатору пользователя
        ------------------------------------------------------------------
        parametrs:
            :user_id: идентификатор пользователя
        '''
        self.cur.execute(
            '''
            SELECT id FROM posts
            WHERE user_id = (?)
            ''',
            (user_id,)
        )
        return self.cur.fetchall()
    
    def select_all_data(self):
        '''Метод получает все данные из таблицы posts'''
        self.cur.execute(
            '''
            SELECT * FROM posts
            '''
        )
        return self.cur.fetchall()
    
    def delete_post(
        self,
        post_id: int
    ) -> None:
        '''
        Метод удаляет пост из таблицы posts по идентефикатору поста
        -----------------------------------------------------------
        parametrs:
            :post_id: идентификатор поста
        '''
        self.cur.execute(
            '''
            DELETE FROM posts
            WHERE id = (?)
            ''',
            (post_id,)
        )
        self.conn.commit()
        logging.info(f'Posts {post_id} has been deleted')
