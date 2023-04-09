from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp, bot
from red_bot.settings.state import AddUser
from red_bot.sql_db import db


@dp.message_handler(state = AddUser.phone)
async def add_phone__cmd_finish(message: types.Message, state: FSMContext):
    # записываем возраст пользователя
    if message.text.isdigit():
        await state.update_data(phone = int(message.text))
    else:
        await message.reply('Необходимы только цифры! Введите Ваш рабочий номер телефона')
        
    # переходим к следуюшему стейту и спрашиваем про пол
    user_data = await state.get_data()
    user_name, user_age, user_phone = user_data.get('name'), user_data.get('age'), user_data.get('phone')
    if user_data.get('gender') == 'Мужской':
        user_gender = 1
    if user_data.get('gender') == 'Женский':
        user_gender = 0
    db.database.insert_users(
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