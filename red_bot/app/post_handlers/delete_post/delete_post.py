from aiogram import types, F
from aiogram.fsm.context import FSMContext


from red_bot.settings.setting import dp
from red_bot.settings.config import CHANNEL_ID
from red_bot.sql_db.posts_db import posts
from red_bot.utils.state import DeletePost
from red_bot.utils.content.text_content import DELETE_POST_MESSAGE


@dp.callback_query(F.data == 'delete_post', F.state == DeletePost.num_post)
async def delete_post(callback: types.CallbackQuery, state: FSMContext) -> None:
    '''
    Метод отображает ссылку с виджетом выбраной записи по её
    номеру и удаляет её.
    ----------------------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) пола пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :callback: тип объекта представления.
        :text: вызов callback_query по ключевому слову.
    '''
    get_num_post = await state.get_data()
    num_post = get_num_post['num_post']
    await callback.bot.delete_message(
        chat_id = CHANNEL_ID,
        message_id = num_post,
    )
    posts.delete_post(num_post)
    await callback.message.answer(
        text = DELETE_POST_MESSAGE,
        reply_markup = types.ReplyKeyboardRemove()
    )
    await state.clear()