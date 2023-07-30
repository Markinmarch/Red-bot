from aiogram import types
from aiogram.dispatcher import FSMContext
import asyncio


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost
from red_bot.utils.keyboards.replay_keyboard import by_agreement
from red_bot.utils.content.text_content import INTERRUPTION_MESSAGE


@dp.message_handler(state = AddPost.text)
async def add_text__cmd_conditions(message: types.Message, state: FSMContext):
    async with state.proxy() as post_data:
        post_data['text'] = message.text
    await AddPost.next()
    await message.answer(
        text = 'Опишите условия работы - зарплату/цену за заказ',
        reply_markup = by_agreement
    )
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(120)
    try:
        check_data = await state.get_data()
        if check_data['text'] != None:
            pass
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.finish()