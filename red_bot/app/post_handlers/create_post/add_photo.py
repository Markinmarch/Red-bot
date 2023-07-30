from aiogram import types
from aiogram.dispatcher import FSMContext
import asyncio


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost
from red_bot.utils.keyboards.inline_keyboard import publish_button
from red_bot.utils.content.text_content import INTERRUPTION_MESSAGE


@dp.message_handler(state = AddPost.photo, content_types = types.ContentType.ANY)
async def add_photo__cmd_publish(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as post_data:
        if message.text == 'Продолжить публикацию':
            post_data['photo'] = 'standart_photo'
        else:
            post_data['photo'] = message.photo[0].file_id
    await message.answer(
        text = 'Теперь Вы можете опубликовать свою запись',
        reply_markup = publish_button
    )
    await asyncio.sleep(60)
    try:
        check_data = await state.get_data()
        if check_data['photo'] != None:
            None
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.finish()