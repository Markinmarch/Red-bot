from aiogram import types


def agree_markup():
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text = '📝 Продолжить', callback_data = 'agree')
    return markup.add(btn)

def registration_markup():
    registration_markup = types.InlineKeyboardMarkup()
    registration_btn = types.InlineKeyboardButton(text = 'Регистрация', callback_data = 'create_account')
    return registration_markup.add(registration_btn)

def authorization_markup():
    authorization_markup = types.InlineKeyboardMarkup()
    authorization_btn = types.InlineKeyboardButton(text = 'Авторизация', callback_data = 'authorization')
    return authorization_markup.add(authorization_btn)

