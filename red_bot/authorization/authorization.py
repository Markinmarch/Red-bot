from aiogram import types
import asyncio


from red_bot.settings.setting import dp
from red_bot.sql_db import db


@dp.message_handler(commands = ['start'])
async def authorization(message: types.Message):
    markup = types.InlineKeyboardMarkup(resize_keyboard = True)
    auth_btn = types.InlineKeyboardButton(text = 'Авторизация', callback_data = 'check_user')
    register_btn = types.InlineKeyboardButton(text = 'Регистрация', callback_data = 'registration')
    markup.add(auth_btn, register_btn)
    await message.answer(text = f'Приветствую, {message.from_user.first_name}!',reply_markup = markup)

@dp.callback_query_handler(text = 'check_user')
async def check_user_id(callback_query: types.CallbackQuery):
    try:
        if callback_query.from_user.id not in db.database.ids_users():
            await callback_query.answer(text = 'Пройдите регистрацию', show_alert = True)
    except TypeError:
        await callback_query.answer(text = 'Пройдите регистрацию', show_alert = True)
    else:
        await callback_query.answer(text = 'Вы зарегестрированный пользователь', show_alert = True)


