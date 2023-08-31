from aiogram import types


from red_bot.settings.setting import dp
from red_bot.settings.config import CHANNEL_URL
from red_bot.utils.content.text_content import FEEDBACK, ALREADY_RESPONDED_MESSAGE, FEEDBACK_SEND
from red_bot.sql_db.posts_db import Posts
from red_bot.sql_db.responders_db import Responders


@dp.callback_query_handler(text = 'respond_to_ad')
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
    if Responders.checking_responses(
        responder_id = callback.from_user.id,
        post_id = callback.message.message_id
    ) != 0:
        await callback.answer(
            text = ALREADY_RESPONDED_MESSAGE,
            show_alert = True
        )
    else:
        Responders.insert_post(
            responder_id = callback.from_user.id,
            post_id = callback.message.message_id
        )
        await callback.answer(
            text = FEEDBACK_SEND,
            show_alert = True
        )
        creator_id = Posts.select_user(callback.message.message_id)
        await callback.bot.send_message(
            chat_id = creator_id[0],
            text = FEEDBACK.format(callback.from_user.url, callback.from_user.full_name, CHANNEL_URL, callback.message.message_id),
            parse_mode = 'HTML'
        )
