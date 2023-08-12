import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.settings.config import CHANNEL_URL
from red_bot.settings.config import TIMEOUT_MESSAGES
from red_bot.utils.keyboards.inline_keyboard import delete_post_button
from red_bot.utils.state import DeletePost


@dp.message_handler(state = DeletePost.num_post)
async def delete_post(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as num_post:
        num_post['num_post'] = message.text
    get_num_post = await state.get_data()
    num_post = get_num_post['num_post']
    await message.answer(
        text = f'<a href = "{CHANNEL_URL}/{num_post}">{num_post}</a>',
        parse_mode = 'HTML',
        reply_markup = delete_post_button
    )
