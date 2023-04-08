from aiogram import types


from red_bot.settings.setting import dp
from red_bot.sql_db import db


@dp.message_handler(commands = ['start'])
async def authorization(message: types.Message):
    markup = types.InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    auth_btn = types.KeyboardButton(text = 'Авторизация')
    register_btn = types.InlineKeyboardButton(text = 'Регистрация', callback_data = '/registration')
    message_for_new_user = await message.answer(
        text = f'Приветствую, {message.from_user.first_name}! Вы не зарегестрированы в боте. Пожалуйста, пройдите регистрацию',
        reply_markup = markup.add(register_btn)
    )
    try:
        if message.from_user.id not in db.database.ids_users():
            message_for_new_user
    except TypeError:
        message_for_new_user
    else:
        await message.answer(text = 'Вы зарегестрированный пользователь')


# @dp.callback_query_handler(run_task = 'registration')
# async def check_user_id(callback_query: types.CallbackQuery):
#     await callback_query.telegram_types
#     await callback_query.message.answer(text = '/registration')
#     try:
#         if callback_query.from_user.id not in db.database.ids_users():
#             await callback_query.answer(text = 'Пройдите регистрацию', show_alert = True)
#     except TypeError:
#         await callback_query.answer(text = 'Пройдите регистрацию', show_alert = True)
#     else:
#         await callback_query.answer(text = 'Вы зарегестрированный пользователь', show_alert = True)


