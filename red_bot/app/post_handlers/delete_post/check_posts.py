import asyncio
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from red_bot.settings.setting import dp
from red_bot.sql_db.posts_db import posts
from red_bot.settings.config import TIMEOUT_MESSAGES
from red_bot.utils.content.text_content import CHECK_POSTS, NONE_POSTS, INTERRUPTION_MESSAGE
from red_bot.utils.state import DeletePost


@dp.message(Command('my_posts'))
async def check_posts(message: types.Message, state: FSMContext) -> None:
    '''
    Метод вызывает по команде пользователя список его записей,
    оставленных им на канале.
    ----------------------------------------------------------
    parametrs:
        :commands: команда, по которой декоратор вызывается
        :message: тип представления данных
    '''
    request_posts_list = posts.select_posts(message.from_user.id)
    ready_posts_list = [num_posts[0] for num_posts in request_posts_list]
    if len(ready_posts_list) == 0:
        await message.answer(
            text = NONE_POSTS
        )
    else:
        keyboard_post_num = []
        for num_post in ready_posts_list:
            num_post_button = types.KeyboardButton(text = str(num_post))
            keyboard_post_num.append(num_post_button)           

        keyboard = types.ReplyKeyboardMarkup(
            keyboard = [keyboard_post_num, [types.KeyboardButton(text = 'Отменить ❌')]],
            resize_keyboard = True
        )

        await state.set_state(DeletePost.num_post)
        await message.answer(
            text = CHECK_POSTS,
            reply_markup = keyboard
        )
        # конструкция для определения времени ожидания ответа от пользователя
        # благодаря осуществляемому способу защищаем сервер от перегрузок
        await asyncio.sleep(TIMEOUT_MESSAGES['delete_post'])
        try:
            current_state = await state.get_state()
            if current_state == 'DeletePost:num_post':
                raise KeyError
        except KeyError:
            await message.answer(
                text = INTERRUPTION_MESSAGE,
                reply_markup = types.ReplyKeyboardRemove()
                )
            await state.clear()
