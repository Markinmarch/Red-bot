from aiogram import types
import logging

from red_bot.settings.setting import dp, bot
from red_bot.sql_db import db


@dp.message_handler(commands = ['start'])
async def authorization(message: types.Message):

    register_markup = types.InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    auth_markup = types.InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    auth_btn = types.InlineKeyboardButton(text = 'Авторизация', callback_data = 'authorization')
    register_btn = types.InlineKeyboardButton(text = 'Регистрация', callback_data = 'create_account')

    try:
        if message.from_user.id not in db.database.ids_users():
            await message.bot.send_message(
                chat_id = message.from_user.id,
                text = f'Приветствую, {message.from_user.first_name}! Вы не зарегистрированный пользователь. Пожалуйста, пройдите регистрацию',
                reply_markup = register_markup.row(register_btn)
            )

    except TypeError:
        await message.bot.send_message(
            chat_id = message.from_user.id,
            text = f'Приветствую, {message.from_user.first_name}! Вы не зарегистрированный пользователь. Пожалуйста, пройдите регистрацию',
            reply_markup = register_markup.row(register_btn)
        )

    else:
        await message.bot.send_message(
            chat_id = message.from_user.id,
            text = 'Вы зарегестрированный пользователь',
            reply_markup = auth_markup.row(auth_btn)
        )
        logging.info(f'User {message.from_user.id} authorization')