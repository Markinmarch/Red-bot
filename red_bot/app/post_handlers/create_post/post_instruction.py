from aiogram import types
from aiogram.utils.exceptions import Throttled


from red_bot.settings.setting import dp
from red_bot.settings.config import COUNT_LIMIT_POSTS, PAUSE_CREATE_POSTS
from red_bot.sql_db.users import users
from red_bot.sql_db.posts import posts
from red_bot.utils.content.text_content import POST_INSTRUCTION, WAITING_MESSAGE, UNREGISTRED_USER, LIMIT_WARNING_PUBLICATION_MESSAGE
from red_bot.utils.keyboards.inline_keyboard import continue_filling_button, start_registration_button


@dp.message_handler(commands=['create_post'])
async def user_rules_reminder(message: types.Message):
    '''
    Данный объект реализует получение согласия от пользователя
    на дальнейшее создание поста через запрос (нажатие кнопки).
    Так же данный объект реализует ограничение подаваемых
    пользователем объявлений и устанавливает паузу в промежутках
    между созданием объявлений.
    ----------------------------------------------------------
    parametrs:
        :commands: команда вызова обработчика
        :callback: тип объекта представления
    '''
    try:
        if users.checking_users(message.from_user.id) == False:
            await message.answer(
                text = UNREGISTRED_USER.format(message.from_user.first_name),
                reply_markup = start_registration_button
            )
        else:
            if posts.check_quantity_posts(message.from_user.id) > COUNT_LIMIT_POSTS:
                await message.answer(
                    text = LIMIT_WARNING_PUBLICATION_MESSAGE
                )
            else:
                await dp.throttle('create_post', rate = PAUSE_CREATE_POSTS)
                await message.answer(
                    text = POST_INSTRUCTION,
                    parse_mode = 'HTML',
                    reply_markup = continue_filling_button
                )
    except Throttled:
        await message.answer(
            text = WAITING_MESSAGE
        )
