'''
Модуль каждый день очищает SQL и NoSQL базы данных
с последующей записью в отдельный файл формата JSON
'''
from . import erase_SQL_Redis
from . import write_to_JSON
from red_bot.settings.config import REDIS_BD, REDIS_HOST, REDIS_PORT
from sql_db.main import users, posts, DB_PATH

# Время сброса данных о постах пользователей на канале и очистка NoSQL
DROP_TIME = '04'

HOUR = 3600

DAY = HOUR * 24

erase_db = erase_SQL_Redis.erase_databases(
    host = REDIS_HOST,
    port = REDIS_PORT,
    db = REDIS_BD
)

forming_datas = write_to_JSON.forming_dicts(
    users_datas = users.select_all_data(),
    posts_datas = posts.select_all_data()
)

write_datas = write_to_JSON.write_data_to_json(
    db_path = DB_PATH,
    forming_datas = forming_datas
)