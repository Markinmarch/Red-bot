from aiogram import types
from aiogram.dispatcher import FSMContext
import asyncio


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost
from red_bot.utils.content.text_content import INTERRUPTION_MESSAGE


@dp.message_handler(state = AddPost.title)
async def add_title__cmd_text(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as post_data:
        post_data['title'] = message.text
    await AddPost.next()
    await message.answer(text = 'Напишите содержание записи с подробностями')
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(30)
    try:
        check_data = await state.get_data()
        if check_data['title'] != None:
            None
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.finish()