from aiogram import types
from aiogram.fsm.context import FSMContext


from red_bot.settings.setting import dp
from red_bot.settings.config import CHANNEL_URL
from red_bot.sql_db.posts_db import posts
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
        await state.update_data(num_post = message.text)
        get_num_post = await state.get_data()
        num_post = get_num_post['num_post']
        if num_post == '0':
            url = CHANNEL_URL['service']
        else:
            url = CHANNEL_URL['market']
        await message.answer(
            text = f'<a href = "{url}/{message.text[1:]}">{message.text}</a>',
            parse_mode = 'HTML',
            reply_markup = delete_post_button
        )
    except KeyError:
        await message.answer(text = FILTERS_MESSAGE['none_this_post'])
        await state.clear()         
