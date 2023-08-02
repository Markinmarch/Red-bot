from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost
from red_bot.settings.config import CHANNEL_ID
from red_bot.sql_db.posts import posts
from red_bot.utils.keyboards.inline_keyboard import under_post_buttons
from red_bot.utils.content.text_content import POST_CONTENT, PUBLICATION_ACCOUNCEMENT


@dp.message_handler(state = AddPost.photo, content_types = types.ContentType.ANY)
async def add_photo__cmd_publish(message: types.Message, state: FSMContext):
    if message.text == 'Продолжить публикацию':
        await state.update_data(photo = 'standart_photo')
    else:
        await state.update_data(photo = message.photo[0].file_id)
    await message.answer(text = PUBLICATION_ACCOUNCEMENT)

    for_post_data = await state.get_data()
    caption = POST_CONTENT.format(
        for_post_data.get('title'),
        for_post_data.get('text'),
        for_post_data.get('conditions')
    )
    if for_post_data.get('photo') == 'standart_photo':
        photo = types.InputFile(path_or_bytesio = 'red_bot/utils/content/media_content/botik.jpg')
    else:
        photo = for_post_data.get('photo')
    msg = await message.bot.send_photo(
        chat_id = CHANNEL_ID,
        photo = photo,
        caption = caption,
        parse_mode = 'HTML',
        reply_markup = under_post_buttons
    )
    channel_msg_id = msg['message_id']

    await types.ReplyKeyboardRemove()

    posts.insert_post(
        post_id = channel_msg_id,
        user_id = message.from_user.id
    )
    await state.finish()