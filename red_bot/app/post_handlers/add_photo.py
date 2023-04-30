from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddRecord
from red_bot.utils.keyboards.inline_keyboard import publish_button
from red_bot.utils.keyboards.replay_keyboard import continue_add_photo_button


@dp.message_handler(state = AddRecord.first_photo, content_types = types.ContentType.PHOTO)
async def add_first_photo__cmd_second_photo(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as user_data:
        user_data['first_photo'] = message.photo[0].file_id
    await AddRecord.next()
    await message.answer(
        text = 'Можете добавить фотографию, либо начать публикацию. Для этого нажмите кнопку "Продолжить"',
        reply_markup = continue_add_photo_button
    )

@dp.message_handler(state = AddRecord.second_photo, content_types = types.ContentType.PHOTO)
async def add_second_photo__cmd_third_photo(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    if message.text == 'Подолжить':
        message.answer(
            text = None,
            reply_markup = publish_button
        )
    else:
        async with state.proxy() as user_data:
            user_data['second_photo'] = message.photo[0].file_id
        await AddRecord.next()
        await message.answer(
            text = 'Можете добавить фотографию, либо начать публикацию. Для этого нажмите кнопку "Продолжить"',
            reply_markup = continue_add_photo_button
        )

@dp.message_handler(state = AddRecord.third_photo, content_types = types.ContentType.PHOTO)
async def add_third_photo__cmd_publish(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    if message.text == 'Подолжить':
        message.answer(
            text = None,
            reply_markup = publish_button
        )
    else:
        async with state.proxy() as user_data:
            user_data['third_photo'] = message.photo[0].file_id
        await message.answer(
            text = 'Готово! Теперь Вы можете опубликовать свой пост на канале',
            reply_markup = publish_button
        )
