from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from red_bot.settings.config import CHANNEL_URL, BOT_URL


agree_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = '📝 Продолжить',
                callback_data = 'user_agree'
            )
        ]
    ]
)

continue_filling_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = '📝 Продолжить',
                callback_data = 'user_informed'
            )
        ]
    ]
)

publish_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Опубликовать',
                callback_data = 'publish'
            )
        ]
    ]
)

start_registration_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Регистрация',
                callback_data = 'create_account'
            )
        ]
    ]
)

authorization_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Авторизация',
                callback_data = 'authorization'
            )
        ]
    ]
)

choosing_direction_buttons = InlineKeyboardMarkup(
    inline_keyboard = [
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
    ]
)

under_post_buttons = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Отозваться',
                callback_data = 'respond_to_ad',
            )
        ],
        [
            InlineKeyboardButton(
                text = 'Бот',
                url = BOT_URL,
                callback_data = 'join_bot'
            )
        ]
    ]
)

