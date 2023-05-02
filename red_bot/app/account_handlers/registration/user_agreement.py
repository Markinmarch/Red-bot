from aiogram import types


from red_bot.settings.setting import dp
from red_bot.sql_db import db
from red_bot.utils.content.text_content import WELCOME, IF_USER_HAVE_ACCOUNT
from red_bot.utils.keyboards.inline_keyboard import agree_button


@dp.callback_query_handler(text = 'create_account')
async def user_agreement_via_query(callback: types.CallbackQuery):
    await callback.message.answer(
        text = WELCOME,
        parse_mode = 'HTML',
        reply_markup = agree_button
    )

@dp.message_handler(commands=['create_account'])
async def user_agreement_via_command(message: types.Message):
    if message.from_user.id in db.database.ids_users():
        await message.answer(
            text = IF_USER_HAVE_ACCOUNT,
            parse_mode = 'HTML'
        )
    else:
        await message.answer(
            text = WELCOME,
            parse_mode = 'HTML',
            reply_markup = agree_button
        )