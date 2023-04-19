from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


agree_button = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(
            text = '📝 Продолжить',
            callback_data = 'agree'
        )
    ]
])

start_registration_button = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(
            text = 'Регистрация',
            callback_data = 'registration'
        )
    ]
])

authorization_button = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(
            text = 'Авторизация',
            callback_data = 'authorization'
        )
    ]
])