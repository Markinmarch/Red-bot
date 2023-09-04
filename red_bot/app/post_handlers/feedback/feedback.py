from aiogram import types, F


from red_bot.settings.setting import dp
from red_bot.settings.config import CHANNEL_URL, BOT_URL
from red_bot.utils.content.text_content import (
    FEEDBACK,
    ALREADY_RESPONDED_MESSAGE,
    FEEDBACK_SEND,
    UNREGISTRED_USER
)
from red_bot.utils.keyboards.inline_keyboard import start_registration_button
from red_bot.sql_db.posts_db import posts
from red_bot.sql_db.users_db import users
from red_bot.sql_db.responders_db import responders


@dp.callback_query(F.data == 'respond_to_ad')
async def feedback_user(callback: types.CallbackQuery) -> None:
    '''
    Данный объект отправяет автору записи (поста)
    уведомление на действие пользователя (на нажатие
    кнопки "Отозваться") с сылкой на его страницу
    -----------------------------------------------
    parametrs:
        :text: вызов callback_query по ключевому слову.
        :callback: тип объекта представления.
    '''
    if users.checking_users(callback.from_user.id) == True:

        if responders.checking_responses(
            responder_id = callback.from_user.id,
            post_id = callback.message.message_id
        ) != 0:
            await callback.answer(
                text = ALREADY_RESPONDED_MESSAGE,
                show_alert = True
            )
        else:
            responders.respond_post(
                responder_id = callback.from_user.id,
                post_id = callback.message.message_id
            )
            await callback.answer(
                text = FEEDBACK_SEND,
                show_alert = True
            )
            creator_id = posts.select_user(callback.message.message_id)
            await callback.bot.send_message(
                chat_id = creator_id[0],
                text = FEEDBACK.format(
                    callback.from_user.url,
                    callback.from_user.full_name,
                    CHANNEL_URL,
                    callback.message.message_id
                ),
                parse_mode = 'HTML'
            )
    
    else:
        await callback.bot.send_message(
            chat_id = callback.from_user.id,
            text = UNREGISTRED_USER,
            reply_markup = start_registration_button
        )
