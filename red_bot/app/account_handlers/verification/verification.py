from aiogram import types
import logging


from red_bot.settings.setting import dp
from red_bot.utils.keyboards.inline_keyboard import authorization_button, start_registration_button
from red_bot.utils.content.text_content import UNREGISTRED_USER, IF_USER_HAVE_ACCOUNT
from red_bot.sql_db import db
from red_bot.utils.commands import set_commands_for_new_user, set_commands_for_users


@dp.message_handler(commands = ['start'])
async def user_verification(message: types.Message):
    try:
        await set_commands_for_new_user(bot = message.bot)
        if message.from_user.id not in db.users_database.ids_users():
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
        await set_commands_for_users(bot = message.bot)
        await message.answer(
            text = IF_USER_HAVE_ACCOUNT,
            reply_markup = authorization_button
        )
        logging.info(f'User {message.from_user.id} authorization')
