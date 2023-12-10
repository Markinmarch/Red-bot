import json
import logging


from red_bot.sql_db import users, posts
from red_bot.settings.config import DB_PATH


def forming_dicts() -> list:
    users_list = []
    for users_data in users.select_all_data():
        user_data = {
            'user': {
                'id': users_data[0],
                'name': users_data[1],
                'age': users_data[2],
                'gender': users_data[3],
                'phone': users_data[4]
            }
        }
        users_list.append(user_data)
    posts_list = []
    for posts_data in posts.select_all_data():
        post_data = {
            'post': {
                'message_id': posts_data[0],
                'user_id': posts_data[1]
            }
        }
        posts_list.append(post_data)
    return [users_list, posts_list]
    
    
def write_data_to_json():

    with open(
        file = f'{DB_PATH}/user_data.json',
        mode = 'w'
    ) as user_json:
        json.dump(
            forming_dicts()[0],
            user_json,
            sort_keys = True,
            indent = 4
        )
    with open(
        file = f'{DB_PATH}/post_data.json',
        mode = 'w'
    ) as post_json:
        json.dump(
            forming_dicts()[1],
            post_json,
            sort_keys = True,
            indent = 4
        )
    
    logging.info('--- Data has been writen to JSON ---')