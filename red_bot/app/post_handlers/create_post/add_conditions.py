from aiogram import types
from aiogram.dispatcher import FSMContext
import asyncio


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost
from red_bot.utils.keyboards.replay_keyboard import continue_publishing
from red_bot.utils.content.text_content import INTERRUPTION_MESSAGE


@dp.message_handler(state = AddPost.conditions)
async def add_conditions__cmd_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as post_data:
        post_data['conditions'] = message.text
    await AddPost.next()
    await message.answer(
        text = 'Можете прикрепить одну фотографию к записи по желанию либо опубликовать свою запись сразу',
        reply_markup = continue_publishing
    )
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(30)
    try:
        check_data = await state.get_data()
        if check_data['direction'] != None:
            pass
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.finish()