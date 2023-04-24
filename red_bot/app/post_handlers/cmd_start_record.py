from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.state import AddRecord
from red_bot.settings.config import CHANNEL_ID
from red_bot.utils.keyboards.replay_keyboard import direction_detection_buttons


@dp.callback_query_handler(text = 'user_informed')
async def cmd_start_record(callback: types.CallbackQuery):
    await AddRecord.direction.set()
    await callback.message.answer(
        text = 'Пожалуйста, определите тему для Вашей записи',
        reply_markup = direction_detection_buttons
    )
