from aiogram import types
from aiogram.fsm.context import FSMContext


from red_bot.settings.setting import dp
from red_bot.settings.config import CHANNEL_ID
from sql_db.main import posts, users
from red_bot.utils.state import AddPost
from red_bot.utils.keyboards.inline_keyboard import under_post_buttons
from red_bot.utils.content.text_content import POST_CONTENT, PUBLICATION_ACCOUNCEMENT


@dp.message(AddPost.photo)
async def add_photo__cmd_publish(message: types.Message, state: FSMContext) -> None:
    '''
    Данный объект записывает в состояние State()
    фотографию объявления, формирует данные,
    публикует на канале и записывает id автора поста
    с id поста в БД и завершает State()
    -----------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) пола пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления
        :content_types: тип данных
    '''
    if message.text == 'Продолжить публикацию':
        await state.update_data(photo = types.FSInputFile(path = 'red_bot/utils/content/media_content/botik.jpg'))
    else:
        await state.update_data(photo = message.photo[0].file_id)

    for_post_data = await state.get_data()
    caption = POST_CONTENT.format(
        for_post_data.get('title'),
        for_post_data.get('text'),
        for_post_data.get('conditions')
    )
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