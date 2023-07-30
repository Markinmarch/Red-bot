from aiogram import types
from aiogram.dispatcher import FSMContext
import asyncio


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost
from red_bot.utils.content.text_content import INTERRUPTION_MESSAGE


@dp.message_handler(state = AddPost.direction)
async def add_direction__cmd_title(message: types.Message, state: FSMContext):
    async with state.proxy() as post_data:
        post_data['direction'] = message.text
    await AddPost.next()
    await message.answer(
        text = 'Напишите краткое описание записи (напр. Подработка/Услуги сантехника/Дрова/Уголь/Вывезти мусор)',
        reply_markup = types.ReplyKeyboardRemove()
    )
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(10)
    try:
        check_data = await state.get_data()
        if check_data['direction'] != None:
            None
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.finish()