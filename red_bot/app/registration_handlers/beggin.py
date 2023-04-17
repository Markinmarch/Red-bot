from aiogram import types


from red_bot.settings.setting import dp
from red_bot.sql_db import db
from red_bot.app.content import text_message


@dp.callback_query_handler(text = 'create_account')
async def user_agreement_via_query(callback: types.CallbackQuery):
    inline_markup = types.InlineKeyboardMarkup(resize_keyboard = True)
    agree_btn = types.InlineKeyboardButton(text = '📝 Продолжить', callback_data = 'agree')
    await callback.message.answer(
        text = text_message.WELCOME,
        parse_mode = 'HTML',
        reply_markup = inline_markup.add(agree_btn)
    )

@dp.message_handler(commands=['create_account'])
async def user_agreement_via_command(message: types.Message):
    inline_markup = types.InlineKeyboardMarkup(resize_keyboard = True)
    agree_btn = types.InlineKeyboardButton(text = '📝 Продолжить', callback_data = 'agree')
    if message.from_user.id in db.database.ids_users():
        await message.answer(text = '<b>У Вас уже имеется учётная запись</b>', parse_mode = 'HTML')
    else:
        await message.answer(
            text = text_message.WELCOME,
            parse_mode = 'HTML',
            reply_markup = inline_markup.add(agree_btn)
        )