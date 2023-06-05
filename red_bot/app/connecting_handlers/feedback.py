from aiogram import types


from red_bot.settings.setting import dp
from red_bot.settings.config import CHANNEL_URL
from red_bot.sql_db import db


@dp.callback_query_handler(text = 'respond_to_ad')
async def feedback_user(callback: types.CallbackQuery):
    await callback.answer(
        text = 'Отзыв отправлен',
        show_alert = True
    )
    creator_id = db.posts_database.select_user(callback.message.message_id)
    await callback.bot.send_message(
        chat_id = creator_id[0],
        text = f'Пользователь <a href="{callback.from_user.url}">{callback.from_user.full_name}</a> отозвался на Ваше <a href="{CHANNEL_URL}/{callback.message.message_id}">объявление</a>.',
        parse_mode = 'HTML'
    )
