from aiogram import types
import logging

from red_bot.settings.setting import dp
from red_bot.sql_db import db


@dp.message_handler(commands = ['start'])
async def authorization(message: types.Message):
    register_markup = types.InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    auth_markup = types.InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    auth_btn = types.InlineKeyboardButton(text = 'Авторизация', callback_data = 'authorization')
    register_btn = types.InlineKeyboardButton(text = 'Регистрация', callback_data = 'registration')
    message_for_new_user = await message.answer(
        text = f'Приветствую, {message.from_user.first_name}! Вы не зарегистрированный пользователь. Пожалуйста, пройдите регистрацию',
        reply_markup = register_markup.row(register_btn)
    )
    
    try:
        if message.from_user.id not in db.database.ids_users():
            message_for_new_user
    except TypeError:
        message_for_new_user
    else:
        await message.answer(
            text = 'Вы зарегестрированный пользователь',
            reply_markup = auth_markup.row(auth_btn)
        )
        logging.info(f'User {message.from_user.id} authorization')


@dp.callback_query_handler(text = 'authorization')
async def authorization_old_user(callback: types.CallbackQuery):
    await callback.answer('Подождите, проходит авторизация.')