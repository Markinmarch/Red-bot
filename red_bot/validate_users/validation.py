import logging
from aiogram import types


from red_bot.settings.setting import dp
from red_bot.sql_db import db


@dp.callback_query_handler()
async def check_user_id(callback_query: types.CallbackQuery):
    if await callback_query.from_user.id not in db.database.check_ids_users():
        from red_bot import register_handlers
    else:
        logging.info(f'Join user {callback_query.from_user.id}')
# async def check_validate(user_id):
#     if db.database.select_users(user_id) is None:
#         from red_bot import register_handlers
#     else:
#         logging.info(f'Join user {user_id}')