import logging
from aiogram import types


from red_bot.settings.setting import dp
from red_bot.sql_db import db


@dp.message_handler(commands = 'start')
async def authorization(message: types.Message | types.CallbackQuery):
    from red_bot.register_handlers import beggin

    # try:
    #     if message.from_user.id not in db.database.ids_users():
    #         from red_bot.register_handlers import beggin
    #     else:
    #         await message.answer('Нихуя сибе!')
    # except:
    #     from red_bot.register_handlers import beggin
