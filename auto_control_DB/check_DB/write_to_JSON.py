import json
import logging


def forming_dicts(
    users_datas: tuple,
    posts_datas: tuple
) -> list:
    '''
    Метод извлекает и формирует данные из SQL базы данных
    ------------------------------------------------------
    parametrs:
        :users_datas: кортеж данных о пользователях
        :posts_datas: кортеж данных о постах пользователей
    '''
    users_list = []
    for users_data in users_datas:
        user_data = {
            'user': {
                'id': users_data[0],
                'phone': users_data[1]
            }
        }
        users_list.append(user_data)
    posts_list = []
    for posts_data in posts_datas:
        post_data = {
            'post': {
                'message_id': posts_data[0],
                'user_id': posts_data[1]
            }
        }
        posts_list.append(post_data)
    return [users_list, posts_list]
    
    
def write_data_to_json(
    db_path: str,
    forming_datas: list
) -> None:
    '''
    Метод записывает данные в общую папку с базой данных,
    полученные после формирования в нужном порядке
    -----------------------------------------------------
    parametrs:
        :db_path: путь к папке с базой данных
        :forming_datas: сформированный список из БД
    '''
    with open(
        file = f'{db_path}/user_data.json',
        mode = 'w'
    ) as user_json:
        json.dump(
            forming_datas[0],
            user_json,
            sort_keys = True,
            indent = 4
        )
    with open(
        file = f'{db_path}/post_data.json',
        mode = 'w'
    ) as post_json:
        json.dump(
            forming_datas[1],
            post_json,
            sort_keys = True,
            indent = 4
        )
    
    logging.info('--- Data has been writen to JSON ---')