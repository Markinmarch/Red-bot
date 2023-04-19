from aiogram import types
import logging

from red_bot.settings.setting import dp
from red_bot.sql_db import db


@dp.message_handler(commands = ['start'])
async def authorization(message: types.Message):
    inline_markup = types.InlineKeyboardMarkup()
    registration_button = types.InlineKeyboardButton(
        text = 'Регистрация',
        callback_data = 'registration'
    )
    authorization_button = types.InlineKeyboardButton(
        text = 'Авторизация',
        callback_data = 'authorization'
        )

    try:
        if message.from_user.id not in db.database.ids_users():
            await message.answer(
                text = f'Приветствую, {message.from_user.first_name}! Вы не зарегистрированный пользователь. Пожалуйста, пройдите регистрацию',
                reply_markup = inline_markup.row(registration_button)
            )

    except TypeError:
        await message.answer(
            text = f'Приветствую, {message.from_user.first_name}! Вы не зарегистрированный пользователь. Пожалуйста, пройдите регистрацию',
            reply_markup = inline_markup.row(registration_button)
        )

    else:
        await message.answer(
            text = 'Вы зарегестрированный пользователь',
            reply_markup = inline_markup.row(authorization_button)
        )
        logging.info(f'User {message.from_user.id} authorization')
