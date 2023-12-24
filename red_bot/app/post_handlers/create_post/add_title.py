from aiogram import types
from aiogram.fsm.context import FSMContext
import asyncio


from ....settings.config import TIMEOUT_MESSAGES
from ....settings.setting import dp
from ....utils.state import AddPost
from ....utils.keyboards.reply_keyboard import canseled
from ....utils.content.text_content import INTERRUPTION_MESSAGE, CREATE_POST_MESSAGE


@dp.message(AddPost.title)
async def add_title__cmd_text(message: types.Message, state: FSMContext) -> None:
    '''
    Данный объект записывает в состояние State()
    короткое описание темы, затем запрашивает
    полное описание объявления
    -----------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) 
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''
    await state.update_data(title = message.text)
    await state.set_state(AddPost.text)
    await message.answer(
        text = CREATE_POST_MESSAGE['text'],
        reply_markup = canseled
        )
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(TIMEOUT_MESSAGES['create_post']['text'])
    try:
        current_state = await state.get_state()
        if current_state == 'AddPost:text':
            raise KeyError
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.clear()