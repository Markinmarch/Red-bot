from aiogram import types
from aiogram import filters

from red_bot.settings.setting import dp
from red_bot.settings.config import CHANNEL_URL


@dp.callback_query_handler(text = 'authorization')
async def choise_directory(callback: types.CallbackQuery):
    inline_markup = types.InlineKeyboardMarkup()

    jobs_btn = types.InlineKeyboardButton(
        text = 'Работа',
        callback_data = 'jobs',
        url = CHANNEL_URL
    )
    services_btn = types.InlineKeyboardButton(
        text = 'Услуги',
        callback_data = 'services',
        url = CHANNEL_URL
    )
    offers_btn = types.InlineKeyboardButton(
        text = 'Предложения',
        callback_data = 'offers',
        url = CHANNEL_URL
        )
    exchanges_btn = types.InlineKeyboardButton(
        text = 'Биржа',
        callback_data = 'exchanges',
        url = CHANNEL_URL
        )
    inline_markup.add(
        jobs_btn,
        services_btn,
        offers_btn,
        exchanges_btn
    )
    await callback.answer(text = 'Подождите, проходит авторизация.')
    await callback.message.answer(
        text = 'Выберите направление',
        reply_markup = inline_markup)
