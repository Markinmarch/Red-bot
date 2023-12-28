from aiogram import types, F
import asyncio
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from ...settings.setting import dp
from ...settings.config import ADMIN_ID, TIMEOUT_MESSAGES
from ...utils.content.text_content import UNREGISTRED_USER, INTERRUPTION_MESSAGE, MESSAGE_TO_ADMIN, BEFORE_TO_SEND_MESSAGE_ADMINS
from ...utils.state import MessageToAdmin
from ...utils.keyboards.inline_keyboard import start_registration_button
from sql_db import users


@dp.message(Command('contact'))
async def contact_with_admins(message: types.Message, state = FSMContext) -> None:
    '''
    Данный объект реализует получение от пользователя сообщения,
    адресованное администрации канала анонимно.
    ----------------------------------------------------------
    parametrs:
        :commands: команда вызова обработчика
        :message: тип объекта представления
    '''
    if users.checking_users(message.from_user.id) == False:
        await message.answer(
            text = UNREGISTRED_USER.format(message.from_user.first_name),
            reply_markup = start_registration_button
        )
    else:
        await state.set_state(MessageToAdmin.message_to_admin)
        await message.answer(
            text = BEFORE_TO_SEND_MESSAGE_ADMINS
        )
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(TIMEOUT_MESSAGES['message_to_admin'])
    try:
        current_state = await state.get_state()
        if current_state == 'MessageToAdmin:message_to_admin':
            raise KeyError
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.clear()


@dp.message(MessageToAdmin.message_to_admin)
async def add_message_to_admin__send(message: types.Message, state: FSMContext) -> None:
    '''
    Данный объект записывает в состояние State()
    сообщение администрации канала, затем отправляет
    его с подписью пользователя администрации
    -----------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) 
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''
    await state.update_data(message_to_admin = message.text)
    await message.answer(text = 'Ваше уведомление отправлено администрации канала')
    for_admin_data = await state.get_data()
    message_to_admin = for_admin_data.get('message_to_admin')
    await message.bot.send_message(
        chat_id = ADMIN_ID,
        text = MESSAGE_TO_ADMIN.format(message.from_user.url, message.from_user.full_name) + f'{message_to_admin}'
    )
    await state.clear()
