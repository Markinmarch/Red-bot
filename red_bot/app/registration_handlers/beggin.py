from aiogram import types


from red_bot.settings.setting import dp
from red_bot.sql_db import db


@dp.callback_query_handler(text = 'create_account')
async def user_agreement_via_query(callback: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup(resize_keyboard = True)
    agree_btn = types.InlineKeyboardButton(text = '📝 Продолжить', callback_data = 'agree')
    markup.add(agree_btn)
    await callback.message.answer(
        text = 'Привет! Я бот, который поможет Вам найти быструю работу или разместить своё объявление с предложением.\n'
        'Но для начала Вам необходимо ознакомиться с некоторыми правилами и юридическими аспектами, чтобы не стать жертвой мошенников.\n'
        'Для этого перейди по <b><a href = "https://telegra.ph/Pravila-polzovaniya-telegram-botom-02-25">ссылке</a></b> и прочти обязательно правила!\n'
        'Ваша дальнейшая регистрация автоматически подтверждает, что Вы ознакомились с правилами.',
        parse_mode = 'HTML',
        reply_markup = markup
    )


@dp.message_handler(commands=['create_account'])
async def user_agreement_via_command(message: types.Message):
    markup = types.InlineKeyboardMarkup(resize_keyboard = True)
    agree_btn = types.InlineKeyboardButton(text = '📝 Продолжить', callback_data = 'agree')
    markup.add(agree_btn)
    if message.from_user.id in db.database.ids_users():
        await message.answer(text = '<b>У Вас уже имеется учётная запись</b>', parse_mode = 'HTML')
    else:
        await message.answer(
            text = 'Привет! Я бот, который поможет Вам найти быструю работу или разместить своё объявление с предложением.\n'
            'Но для начала Вам необходимо ознакомиться с некоторыми правилами и юридическими аспектами, чтобы не стать жертвой мошенников.\n'
            'Для этого перейди по <b><a href = "https://telegra.ph/Pravila-polzovaniya-telegram-botom-02-25">ссылке</a></b> и прочти обязательно правила!\n'
            'Ваша дальнейшая регистрация автоматически подтверждает, что Вы ознакомились с правилами.',
            parse_mode = 'HTML',
            reply_markup = markup
        )