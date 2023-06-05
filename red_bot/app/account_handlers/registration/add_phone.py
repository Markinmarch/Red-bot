import logging
from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp, bot
from red_bot.utils.state import AddUser
from red_bot.sql_db import db
from red_bot.utils.commands import set_commands_for_users


@dp.message_handler(state = AddUser.phone)
async def add_phone__cmd_finish(message: types.Message, state: FSMContext):
    auth_markup = types.InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    auth_btn = types.InlineKeyboardButton(text = 'Авторизация', callback_data = 'authorization')
    # записываем возраст пользователя
    if message.text.isdigit():
        await state.update_data(phone = int(message.text))
    else:
        await message.answer('Необходимы только цифры! Введите Ваш рабочий номер телефона')

    user_data = await state.get_data()
    user_name, user_age, user_phone = user_data.get('name'), user_data.get('age'), user_data.get('phone')
    if user_data.get('gender') == 'Мужской':
        user_gender = 1
    if user_data.get('gender') == 'Женский':
        user_gender = 0
    db.users_database.insert_users(
        message.from_user.id,
        user_name,
        user_age,
        user_gender,
        user_phone
    )

    await bot.send_message(
        message.chat.id,
        text = f'Привет, {user_name}, {user_age}, {user_phone}, {user_gender}'
        )
    await state.finish()
    logging.info(f'User {message.from_user.id} authorization')
    await set_commands_for_users(bot = message.bot)