from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.settings.setting import bot
from red_bot.utils.state import AddRecord
from red_bot.settings.config import CHANNEL_ID
from red_bot.utils.keyboards.inline_keyboard import under_post_buttons


@dp.callback_query_handler(text = 'publish', state = AddRecord)
async def user_publish_post(callback: types.CallbackQuery, state: FSMContext):
    post_data = await state.get_data()
    media = types.MediaGroup()
    media.attach_photo(types.InputMediaPhoto(
        post_data.get('first_photo'),
        caption = (
            f'<b>{post_data.get("direction")}: <u>{post_data.get("title")}</u></b>\n'
            f'→ {post_data.get("text")}\n'
            f'→ <i>{post_data.get("conditions")}</i>'
        )
    ))
    media.attach_photo(types.InputMediaPhoto(post_data.get('second_photo')))
    media.attach_photo(types.InputMediaPhoto(post_data.get('third_photo')))
    await callback.bot.send_media_group(
        chat_id = CHANNEL_ID,
        media = media
        # reply_markup = under_post_buttons
    )
    # await callback.bot.send_message(
    #     chat_id = CHANNEL_ID,
    #     text = 'callback.from_user.first_name',
    #     reply_markup = under_post_buttons,
    # )
    await state.finish()
