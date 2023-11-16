from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


direction_detection_buttons = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'Услуга'
            ),
            KeyboardButton(
                text = 'Биржа'
            )
        ],
        [
            KeyboardButton(
                text = 'Отменить ❌'
            )
        ]
    ],
    one_time_keyboard = True,
    is_persistent = True,
    resize_keyboard = True,
    input_field_placeholder = 'Тема для публикации записи',
)

choose_gender = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'Мужской'
            )
        ],
        [
            KeyboardButton(
                text = 'Женский'
            )
        ],
        [
            KeyboardButton(
                text = 'Отменить ❌'
            )
        ]
    ],
    one_time_keyboard = True,
    is_persistent = True,
    resize_keyboard = True,
    input_field_placeholder = 'Пол пользователя',
)

get_phone_user = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'Да! Отправить телефон',
                request_contact = True
            )
        ],
        [
            KeyboardButton(
                text = 'Отменить ❌'
            )
        ]
    ],
    one_time_keyboard = True,
    is_persistent = True,
    resize_keyboard = True  
)

continue_publishing = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'Продолжить публикацию'
            )
        ],
        [
            KeyboardButton(
                text = 'Отменить ❌'
            )
        ]
    ],
    one_time_keyboard = True,
    is_persistent = True,
    resize_keyboard = True,
    input_field_placeholder = 'Прикрепите фото'
)

by_agreement = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'По договорённости'
            )
        ],
        [
            KeyboardButton(
                text = 'Отменить ❌'
            )
        ]
    ],
    one_time_keyboard = True,
    is_persistent = True,
    resize_keyboard = True,
    input_field_placeholder = 'Введите стоимость либо нажмите кнопку'
)

canseled = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'Отменить ❌'
            )
        ]
    ],
    one_time_keyboard = True,
    is_persistent = True,
    resize_keyboard = True
)