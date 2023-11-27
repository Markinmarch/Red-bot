import asyncio
from aiogram import types
from aiogram.fsm.context import FSMContext


from red_bot.settings.setting import dp
from red_bot.settings.config import TIMEOUT_MESSAGES
from red_bot.utils.state import AddPost
from red_bot.utils.keyboards.reply_keyboard import canseled
from red_bot.utils.content.text_content import INTERRUPTION_MESSAGE, CREATE_POST_MESSAGE


@dp.message(AddPost.direction)
async def add_direction__cmd_title(message: types.Message, state: FSMContext) -> None:
    '''
    Данный объект записывает в состояние State()
    выбранное название темы, затем запрашивает
    короткое описание объявления
    -----------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) пола пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''
    await state.update_data(direction = message.text)
    await state.set_state(AddPost.title)
    await message.answer(
        text = CREATE_POST_MESSAGE['title'],
        reply_markup = canseled
    )
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(TIMEOUT_MESSAGES['create_post']['title'])
    try:
        current_state = await state.get_state()
        if current_state == 'AddPost:title':
            raise KeyError
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.clear()
