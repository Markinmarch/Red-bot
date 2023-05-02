from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddRecord
from red_bot.utils.keyboards.inline_keyboard import publish_button


@dp.message_handler(state = AddRecord.photo, content_types = types.ContentType.ANY)
async def add_photo__cmd_publish(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as from_user_data:
        if message.text == 'Продолжить публикацию':
            from_user_data['photo'] = None
        else:
            from_user_data['photo'] = message.photo[0].file_id
    await message.answer(
        text = 'Теперь Вы можете опубликовать свою запись',
        reply_markup = publish_button
    )
