from aiogram import types
from aiogram.fsm.context import FSMContext


from red_bot.settings.setting import dp
from red_bot.settings.config import CHANNEL_URL
from red_bot.sql_db import posts
from red_bot.utils.content.text_content import FILTERS_MESSAGE
from red_bot.utils.keyboards.inline_keyboard import delete_post_button
from red_bot.utils.state import DeletePost


@dp.message(DeletePost.num_post)
async def show_post(message: types.Message, state: FSMContext) -> None:
    '''
    Метод отображает список номеров id записей пользователя.
    ----------------------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) пола пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объекта представления.
    '''
    try:
        request_posts_list = posts.select_posts(message.from_user.id)
        ready_posts_list = [num_posts[0] for num_posts in request_posts_list]
        if int(message.text) not in ready_posts_list:
            raise TypeError
        await state.update_data(num_post = int(message.text))
        await message.answer(
            text = f'<a href = "{CHANNEL_URL}/{message.text}">{message.text}</a>',
            parse_mode = 'HTML',
            reply_markup = delete_post_button
        )
        
    except TypeError:
        await message.answer(
            text = FILTERS_MESSAGE['none_this_post'],
            reply_markup = types.ReplyKeyboardRemove()
        )
        await state.clear()         
