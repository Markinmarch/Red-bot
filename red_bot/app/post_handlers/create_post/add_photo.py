from aiogram import types
from aiogram.fsm.context import FSMContext


from ....settings.setting import dp
from ....settings.config import CHANNEL_ID
from ....utils.state import AddPost
from ....utils.keyboards.inline_keyboard import under_post_buttons
from ....utils.content.text_content import POST_CONTENT, PUBLICATION_ACCOUNCEMENT
from sql_db import posts, users


@dp.message(AddPost.photo)
async def add_photo__cmd_publish(message: types.Message, state: FSMContext) -> None:
    '''
    Данный объект записывает в состояние State()
    фотографию объявления, формирует данные,
    публикует на канале и записывает id автора поста
    с id поста в БД и завершает State()
    -----------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) 
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления
        :content_types: тип данных
    '''
    for_post_data = await state.get_data()
    caption = POST_CONTENT.format(
        for_post_data.get('title'),
        for_post_data.get('text'),
        for_post_data.get('conditions')
    )
    # если пользователь нажал кнопку "Продолжить публикацию" - тогда просто публикуется сообщение
    if message.text == 'Продолжить публикацию':
        msg = await message.bot.send_message(
            chat_id = CHANNEL_ID,
            text = caption,
            reply_markup = under_post_buttons
        )
    else:
        await state.update_data(photo = message.photo[0].file_id)
        photo = for_post_data.get('photo')
        msg = await message.bot.send_photo(
            chat_id = CHANNEL_ID,
            photo = photo,
            caption = caption,
            parse_mode = 'HTML',
            reply_markup = under_post_buttons
        )
    await message.answer(
        text = PUBLICATION_ACCOUNCEMENT,
        reply_markup = types.ReplyKeyboardRemove()
        )
    
    # записываем id поста и id пользователя в БД
    posts.insert_post(
        post_id = msg.message_id,
        user_id = message.from_user.id
    )
    # тут добавили +1 к количеству сообщений закреплённыз за этим пользователем
    users.add_one_message(message.from_user.id)
    await state.clear()