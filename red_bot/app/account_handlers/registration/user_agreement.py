from aiogram import types, F
import logging
from aiogram.filters import Command


from ....settings.setting import dp
from ....utils.content.text_content import WELCOME, IF_USER_HAVE_ACCOUNT, UPDATE_MESSAGE
from ....utils.keyboards.inline_keyboard import agree_button
from .....sql_db.main import users


@dp.callback_query(F.data == 'create_account')
async def user_agreement_via_query(callback: types.CallbackQuery) -> None:
    '''
    Данный объект реализует получение согласия от пользователя
    на дальнейшую регистрацию через запрос (нажатие кнопки)
    ----------------------------------------------------------
    parametrs:
        :F.data: фильтр обратного вызова обработчика
        :callback: тип объекта представления
    '''
    await callback.message.answer(
        text = WELCOME,
        parse_mode = 'HTML',
        reply_markup = agree_button
    )

@dp.message(Command('create_account'))
async def user_agreement_via_command(message: types.Message) -> None:
    '''
    Данный объект реализует получение согласия от пользователя
    на дальнейшую регистрацию через команду
    ----------------------------------------------------------
    parametrs:
        :commands: команда вызова обработчика
        :message: тип объекта представления
    '''
    if users.checking_users(message.from_user.id) == False:
        await message.answer(
            text = WELCOME,
            parse_mode = 'HTML',
            reply_markup = agree_button
        )
    else:
        await message.answer(
            text = IF_USER_HAVE_ACCOUNT +'\n'+ UPDATE_MESSAGE
        )
        logging.info(f'User {message.from_user.id} authorization')