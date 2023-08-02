from aiogram import types
from aiogram.dispatcher import FSMContext
import asyncio


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost
from red_bot.utils.content.text_content import INTERRUPTION_MESSAGE


@dp.message_handler(state = AddPost.title)
async def add_title__cmd_text(message: types.Message, state: FSMContext):
    await state.update_data(title = message.text)
    await AddPost.next()
    await message.answer(text = 'Напишите содержание записи с подробностями')
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(10)
    try:
        current_state = await state.get_state()
        if current_state == 'AddPost:text':
            raise KeyError
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.finish()