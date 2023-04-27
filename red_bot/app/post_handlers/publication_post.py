from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddRecord
from red_bot.settings.config import CHANNEL_ID


@dp.callback_query_handler(text = 'publish', state = AddRecord)
async def user_publish_post(callback: types.CallbackQuery, state: FSMContext):
    post_data = await state.get_data()
    await callback.bot.send_photo(
        chat_id = CHANNEL_ID,
        photo = post_data.get("photo"),
        caption = (f'<b>{post_data.get("title")}</b> \n {post_data.get("text")} \n {post_data.get("conditions")}'),
        parse_mode = 'HTML'
    )
    await state.finish()
    