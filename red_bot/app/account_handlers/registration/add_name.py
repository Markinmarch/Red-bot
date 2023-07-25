from aiogram import types
from aiogram.dispatcher import FSMContext
import asyncio


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser
from red_bot.utils.content.text_content import INTERRUPTION_MESSAGE, REGISTRATION_MESSAGE


@dp.message_handler(state = AddUser.name)
async def add_name__cmd_age(message: types.Message, state: FSMContext) -> None:
    '''
    Данный объект записывает в состояние State()
    имя нового пользователя и переходит к следующему
    состоянию, запрашивающему возраст пользователя
    -----------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) имени пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''
    async with state.proxy() as user_data:
        user_data['name'] = message.text
    await AddUser.next()
    await message.answer(text = REGISTRATION_MESSAGE['add_age'])
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(12)
    try:
        data = await state.get_data()
        if data['age'] != None:
            pass
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.finish()