from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from red_bot.settings.config import CHANNEL_URL


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
            callback_data = 'create_account'
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

choosing_directions_button = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(
            text = 'Предложения',
            callback_data = 'offers',
            url = CHANNEL_URL
        )
    ],
    [
        InlineKeyboardButton(
            text = 'Услуги',
            callback_data = 'services',
            url = CHANNEL_URL
        )
    ],
    [
        InlineKeyboardButton(
            text = 'Биржа',
            callback_data = 'exchange',
            url = CHANNEL_URL
        )
    ]
])
