from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddRecord
from red_bot.utils.keyboards.inline_keyboard import publish_button
from red_bot.settings.config import CHANNEL_ID


@dp.message_handler(state = AddRecord.price)
async def add_price__cmd_finish(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as user_data:
        user_data['price'] = message.text
    await message.answer(
        text = 'Готово! Теперь Вы можете опубликовать свой пост на канале',
        reply_markup = publish_button
    )