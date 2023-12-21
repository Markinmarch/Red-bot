from aiogram import types
from aiogram.fsm.context import FSMContext
import asyncio


from ....settings.config import TIMEOUT_MESSAGES
from ....settings.setting import dp
from ....utils.state import AddPost
from ....utils.keyboards.reply_keyboard import by_agreement
from ....utils.content.text_content import INTERRUPTION_MESSAGE, CREATE_POST_MESSAGE


@dp.message(AddPost.text)
async def add_text__cmd_conditions(message: types.Message, state: FSMContext) -> None:
    '''
    Данный объект записывает в состояние State()
    полно описание объявления, затем запрашивает
    условия. Если пользователь не может/не знает
    на данный момент условий - может нажать на
    кнопку "По договорённости"
    -----------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) пола пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''
    await state.update_data(text = message.text)
    await state.set_state(AddPost.conditions)
    await message.answer(
        text = CREATE_POST_MESSAGE['conditions'],
        reply_markup = by_agreement
    )
    await asyncio.sleep(TIMEOUT_MESSAGES['create_post']['conditions'])
    try:
        current_state = await state.get_state()
        if current_state == 'AddPost:conditions':
            raise KeyError
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.clear()