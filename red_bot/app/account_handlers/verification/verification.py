from aiogram import types
import logging

from red_bot.settings.setting import dp
from red_bot.utils.keyboards.inline_keyboard import authorization_button, start_registration_button
from red_bot.utils.content.text_content import UNREGISTRED_USER, IF_USER_HAVE_ACCOUNT
from red_bot.sql_db import db
from red_bot.utils.commands import set_commands


@dp.message_handler(commands = ['start', 'create_account'])
async def user_verification(message: types.Message):
    try:
        if message.from_user.id not in db.database.ids_users():
            await message.answer(
                text = UNREGISTRED_USER.format(message.from_user.first_name),
                reply_markup = start_registration_button
            )

    except TypeError:
        await message.answer(
            text = UNREGISTRED_USER.format(message.from_user.first_name),
            reply_markup = start_registration_button
        )

    else:
        await message.answer(
            text = IF_USER_HAVE_ACCOUNT,
            reply_markup = authorization_button
        )
        logging.info(f'User {message.from_user.id} authorization')
    await set_commands(bot = message.bot)
