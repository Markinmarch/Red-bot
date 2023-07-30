from aiogram import types
import asyncio
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost
from red_bot.utils.keyboards.replay_keyboard import direction_detection_buttons
from red_bot.utils.content.text_content import INTERRUPTION_MESSAGE


@dp.callback_query_handler(text = 'user_informed')
async def cmd_start_record(callback: types.CallbackQuery, state = FSMContext):
    await AddPost.direction.set()
    await callback.message.answer(
        text = 'Пожалуйста, определите тему для Вашей записи',
        reply_markup = direction_detection_buttons
    )
