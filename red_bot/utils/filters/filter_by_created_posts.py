from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.keyboards.replay_keyboard import direction_detection_buttons
from red_bot.utils.state import AddPost


@dp.message_handler(
    lambda message: message.text not in direction_detection_buttons.__str__,
    state = AddPost.direction
)
async def repeat_enter_direction(message: types.Message):
    await message.answer(
        text = 'Пожалуйста, выберите вариант из представленных.'
    )
    
@dp.message_handler(
    lambda message: len(message.text) > 20,
    state = AddPost.title
)
async def repeat_enter_title(message: types.Message):
    await message.answer(
        text = 'Пожалуйста, опишите деятельность короче'
    )

@dp.message_handler(
    lambda message: len(message.text) < 10,
    state = AddPost.text
)
async def repeat_enter_text(message: types.Message):
    await message.answer(
        text = 'Пожалуйста, опишите деятельность подробнее.'
    )
