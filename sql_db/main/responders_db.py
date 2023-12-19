import logging


from . bot_tables import Bot_tables_DB

class Responders(Bot_tables_DB):
    '''
    Объект наследует основной класс :Bot_tables_DB:
    Данный класс реализован с целью управления таблицей
    :responders: по методу CRUD
    '''
    def __init__(self):
        super().__init__()

    def respond_post(
        self,
        responder_id: int,
        post_id: int
    ):
        '''
        Метод добавляет в таблицу responders запись отзыва пользователей на пост
        ------------------------------------------------------------------------
        parametrs:
            :responders_id: идентификатор пользователя, который отозвался на пост
            :post_id: идентификатор поста пользователя
        '''
        self.cur.execute(
            '''
            INSERT INTO responders (
                responder_id,
                post_id
            )
            VALUES (?, ?);            
            ''',
            (
                responder_id,
                post_id
            )
        )
        self.conn.commit()
        logging.info(f'User -- id: {responder_id} -- respond a post: {post_id}')

    def checking_responses(
        self,
        responder_id: int,
        post_id: int
    ):
        '''
        Метод определяет наличие записи в таблице
        -----------------------------------------
        parametrs:
            :responders_id: идентификатор пользователя, который отозвался на пост
            :post_id: идентификатор поста пользователя
        '''
        self.cur.execute(
            '''
            SELECT COUNT(*) FROM responders
            WHERE responder_id = ? AND post_id = ?
            ''',
            (
                responder_id,
                post_id
            )
        )
        return self.cur.fetchone()[0]
