from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddRecord
from red_bot.settings.config import CHANNEL_ID
from red_bot.utils.keyboards.inline_keyboard import under_post_buttons


@dp.callback_query_handler(text = 'publish', state = AddRecord)
async def user_publish_post(callback: types.CallbackQuery, state: FSMContext):
    from_user_data = await state.get_data()
    await callback.bot.send_photo(
        chat_id = CHANNEL_ID,
        photo = from_user_data.get('photo'),
        caption = (
            f'<b>{from_user_data.get("direction")}: <u>{from_user_data.get("title")}</u></b>\n'
            f'→ {from_user_data.get("text")}\n'
            f'→ <i>{from_user_data.get("conditions")}</i>'
        ),
        parse_mode = 'HTML',
        reply_markup = under_post_buttons
    )
    await state.finish()
