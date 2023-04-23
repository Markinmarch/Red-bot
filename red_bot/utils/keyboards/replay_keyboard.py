from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


direction_detection_buttons = ReplyKeyboardMarkup(
    keyboard = [
    [
        KeyboardButton(
            text = 'Предложения',
        )
    ],
    [
        KeyboardButton(
            text = 'Услуги'
        )
    ],
    [
        KeyboardButton(
            text = 'Биржа'
        )
    ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True,
    input_field_placeholder = 'Тема для публикации записи',
    selective = True
)