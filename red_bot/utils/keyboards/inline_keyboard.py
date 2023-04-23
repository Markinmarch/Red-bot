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

choosing_direction_buttons = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(
            text = 'Предложения',
            callback_data = 'offers',
        )
    ],
    [
        InlineKeyboardButton(
            text = 'Услуги',
            callback_data = 'services',
        )
    ],
    [
        InlineKeyboardButton(
            text = 'Биржа',
            callback_data = 'exchange',
        )
    ]
])
