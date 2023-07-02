from aiogram import types
from aiogram.utils.exceptions import Throttled


from red_bot.settings.setting import dp
from red_bot.sql_db import users_db
from red_bot.utils.content.text_content import POST_INSTRUCTION, WAITING_MESSAGE, UNREGISTRED_USER
from red_bot.utils.keyboards.inline_keyboard import continue_filling_button, start_registration_button


@dp.message_handler(commands=['create_post'])
async def user_rules_reminder(message: types.Message):
    try:
        if message.from_user.id not in users_db.users_database.ids_users():
            pass
        await dp.throttle('create_post', rate = 300)
    except Throttled:
        await message.answer(
            text = WAITING_MESSAGE
        )
    except TypeError:
        await message.answer(
            text = UNREGISTRED_USER.format(message.from_user.first_name),
            reply_markup = start_registration_button
        )
    else:
        await message.answer(
            text = POST_INSTRUCTION,
            parse_mode = 'HTML',
            reply_markup = continue_filling_button
        )
