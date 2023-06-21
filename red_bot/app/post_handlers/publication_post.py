from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost
from red_bot.settings.config import CHANNEL_ID
from red_bot.utils.keyboards.inline_keyboard import under_post_buttons
from red_bot.utils.content.text_content import POST_CONTENT, PUBLICATION_ACCOUNCEMENT
from red_bot.sql_db import db


@dp.callback_query_handler(text = 'publish', state = AddPost)
async def user_publish_post(callback: types.CallbackQuery, state: FSMContext):
    from_user_data = await state.get_data()
    caption = POST_CONTENT.format(
        from_user_data.get('title'),
        from_user_data.get('text'),
        from_user_data.get('conditions')
    )
    if from_user_data.get('photo') == None:
        msg = await callback.bot.send_animation(
            chat_id = CHANNEL_ID,   
            animation = types.InputFile('red_bot/utils/content/media_content/standart.gif'),
            caption = caption,
            parse_mode = 'HTML',
            reply_markup = under_post_buttons
        )
        channel_msg_id = msg['message_id']
    else:
        msg = await callback.bot.send_photo(
            chat_id = CHANNEL_ID,
            photo = from_user_data.get('photo'),
            caption = caption,
            parse_mode = 'HTML',
            reply_markup = under_post_buttons
        )
        channel_msg_id = msg['message_id']

    db.posts_database.insert_post(
        post_id = channel_msg_id,
        user_id = callback.from_user.id
    )
    await state.finish()
    # убираем все лишние кнопки
    await callback.message.answer(
        text = PUBLICATION_ACCOUNCEMENT,
        reply_markup = types.ReplyKeyboardRemove()
    )