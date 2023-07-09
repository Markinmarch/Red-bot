from aiogram import types


from red_bot.settings.setting import dp
from red_bot.settings.config import CHANNEL_URL
from red_bot.utils.content.text_content import FEEDBACK, ALREADY_RESPONDED_MESSAGE
from red_bot.sql_db.posts import posts
from red_bot.sql_db.responders import responders

@dp.callback_query_handler(text = 'respond_to_ad')
async def feedback_user(callback: types.CallbackQuery):
    """
    Этот объект отправляет автору статьи (поста) уведомление на действие
    пользователя (на нажатие кнопки "Отозваться") с ссылкой на его страницу.
    Пользователь может отозваться на пост автора один раз. (защита от спама)
        :text: ключ/команда вызова функции
        :callback: тип объекта представления
    """
    check_responders = responders.checking_responses(callback.from_user.id, callback.message.message_id)

    if check_responders == False:
        responders.insert_post(
            responder_id = callback.from_user.id,
            post_id = callback.message.message_id
        )
        await callback.answer(
            text = 'Отзыв отправлен',
            show_alert = True
        )
        creator_id = posts.select_user(callback.message.message_id)
        await callback.bot.send_message(
            chat_id = creator_id[0],
            text = FEEDBACK.format(callback.from_user.url, callback.from_user.full_name, CHANNEL_URL, callback.message.message_id),
            parse_mode = 'HTML'
        )
    else:
        await callback.answer(
            text = ALREADY_RESPONDED_MESSAGE,
            show_alert = True
        )
