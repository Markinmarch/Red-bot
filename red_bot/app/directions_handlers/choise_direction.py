from aiogram import types
from aiogram import filters

from red_bot.settings.setting import dp
from red_bot.utils.keyboards.inline_keyboard import choosing_direction_buttons


@dp.callback_query_handler(text = 'authorization')
async def choise_directory(callback: types.CallbackQuery):
    await callback.answer(text = 'Вы авторизованы')
    await callback.message.answer(
        text = 'Выберите направление',
        reply_markup = choosing_direction_buttons)
