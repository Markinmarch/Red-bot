from aiogram import types, F
import asyncio
from aiogram.fsm.context import FSMContext


from ....settings.config import TIMEOUT_MESSAGES
from ....settings.setting import dp
from ....utils.state import AddPost
from ....utils.keyboards.reply_keyboard import title_detection_buttons
from ....utils.content.text_content import INTERRUPTION_MESSAGE, CREATE_POST_MESSAGE


@dp.callback_query(F.data == 'user_informed')
async def cmd_start_create_post(callback: types.CallbackQuery, state = FSMContext) -> None:
    '''
    Данный объект инициализирует состояние State()
    и предлагает выбрать тему объявления
    -----------------------------------------------
    parametrs:
        :text: фильтр обратного вызова обработчика
        :state: (str) параметр состояния конечного автомата (FSMContext)
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''
    await state.set_state(AddPost.title)
    await callback.message.answer(
        text = CREATE_POST_MESSAGE['title'],
        reply_markup = title_detection_buttons
    )
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(TIMEOUT_MESSAGES['create_post']['title'])
    try:
        current_state = await state.get_state()
        if current_state == 'AddPost:title':
            raise KeyError
    except KeyError:
        await callback.message.answer(text = INTERRUPTION_MESSAGE)
        await state.clear()
