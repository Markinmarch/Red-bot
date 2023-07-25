from aiogram import types
from aiogram.dispatcher import FSMContext
import asyncio


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser
from red_bot.utils.keyboards.replay_keyboard import get_phone_user
from red_bot.utils.content.text_content import INTERRUPTION_MESSAGE, REGISTRATION_MESSAGE


@dp.message_handler(state = AddUser.gender)
async def add_gender__cmd_phone(message: types.Message, state: FSMContext):
    '''
    Данный объект записывает в состояние State()
    пол нового пользователя и переходит к следующему
    состоянию, запрашивающему разрешение на получение
    контактных данных пользователя (телефон аккаунта)
    -----------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) пола пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''    
    await state.update_data(gender = message.text)
    await AddUser.next()
    await message.answer(
        text = REGISTRATION_MESSAGE['add_phone'],
        reply_markup = get_phone_user
    )
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(12)
    try:
        data = await state.get_data()
        if data['gender'] != None:
            pass
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.finish()
