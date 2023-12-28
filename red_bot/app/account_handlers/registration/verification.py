from aiogram import types
from aiogram.filters import CommandStart
import logging


from ....settings.setting import dp
from ....utils.keyboards.inline_keyboard import start_registration_button
from ....utils.content.text_content import UNREGISTRED_USER, IF_USER_HAVE_ACCOUNT, UPDATE_MESSAGE
from ....utils.commands import set_commands_for_users
from sql_db import users


@dp.message(CommandStart())
async def user_verification(message: types.Message) -> None:
    '''
    Данный объект проверяет пользователя на наличие
    его учётной запси по его id при первичном запросе
    к телеграм-боту
    -----------------------------------------------
    parametrs:
        :CommandStart: команда вызова обработчика при старте
        :message: тип объкета представления.
    '''
    if users.checking_users(message.from_user.id) == False:
        await set_commands_for_users(bot = message.bot)
        await message.answer(
            text = UNREGISTRED_USER.format(message.from_user.first_name),
            reply_markup = start_registration_button
        )
    else:
        await set_commands_for_users(bot = message.bot)
        await message.answer(
            text = IF_USER_HAVE_ACCOUNT +'\n'+ UPDATE_MESSAGE,
        )
        logging.info(f'User {message.from_user.id} authorization')
