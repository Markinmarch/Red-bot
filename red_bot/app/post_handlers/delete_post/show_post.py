from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageToDeleteNotFound


from red_bot.settings.setting import dp
from red_bot.settings.config import CHANNEL_URL
from red_bot.sql_db.posts_db import posts
from red_bot.utils.content.text_content import NONE_THIS_POST
from red_bot.utils.keyboards.inline_keyboard import delete_post_button
from red_bot.utils.state import DeletePost


@dp.message_handler(state = DeletePost.num_post)
async def show_post(message: types.Message, state: FSMContext) -> None:
    request_posts_list = posts.select_posts(message.from_user.id)
    ready_posts_list = [num_posts[0] for num_posts in request_posts_list]
    if int(message.text) in ready_posts_list:
        async with state.proxy() as num_post:
            num_post['num_post'] = message.text
        get_num_post = await state.get_data()
        num_post = get_num_post['num_post']
        await message.answer(
            text = f'<a href = "{CHANNEL_URL}/{num_post}">{num_post}</a>',
            parse_mode = 'HTML',
            reply_markup = delete_post_button
        )
    else:
        await message.answer(text = NONE_THIS_POST)
        await state.finish()            
