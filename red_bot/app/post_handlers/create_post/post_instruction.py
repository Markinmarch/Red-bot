from aiogram import types
from aiogram.filters import Command


from red_bot.settings.setting import dp
from red_bot.settings.config import COUNT_LIMIT_POSTS
from red_bot.sql_db import users
from red_bot.utils.content.text_content import POST_INSTRUCTION, UNREGISTRED_USER, LIMIT_WARNING_PUBLICATION_MESSAGE
from red_bot.utils.keyboards.inline_keyboard import continue_filling_button, start_registration_button


@dp.message(Command('create_post'))
async def user_rules_reminder(message: types.Message) -> None:
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
    if users.checking_users(message.from_user.id) == False:
        await message.answer(
            text = UNREGISTRED_USER.format(message.from_user.first_name),
            reply_markup = start_registration_button
        )
    else:
        if users.select_quantity_messages(user_id = message.from_user.id) >= COUNT_LIMIT_POSTS:
            await message.answer(
                text = LIMIT_WARNING_PUBLICATION_MESSAGE
            )
        else:
            await message.answer(
                text = POST_INSTRUCTION,
                parse_mode = 'HTML',
                reply_markup = continue_filling_button
            )
