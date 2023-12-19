from aiogram import types, F
from aiogram.fsm.context import FSMContext


from ....settings.setting import dp
from ....settings.config import CHANNEL_ID
from ....utils.state import DeletePost
from ....utils.content.text_content import DELETE_POST_MESSAGE
from sql_db.main import posts


@dp.callback_query(DeletePost.num_post, F.data == 'delete_post')
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
    #удаление записи из БД таблицы posts
    posts.delete_post(post_id = num_post)

    await callback.bot.delete_message(
        chat_id = CHANNEL_ID,
        message_id = num_post
    )
    
    await callback.message.answer(
        text = DELETE_POST_MESSAGE,
        reply_markup = types.ReplyKeyboardRemove()
    )
    await state.clear()