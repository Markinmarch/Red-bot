from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


direction_detection_buttons = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'Предложениe'
            )
        ],
        [
            KeyboardButton(
                text = 'Услуга'
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

continue_publishing = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'Продолжить публикацию'
            )
        ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True,
    selective = True    
)