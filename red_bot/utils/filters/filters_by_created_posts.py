from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.keyboards.reply_keyboard import direction_detection_buttons
from red_bot.utils.state import AddPost
from red_bot.utils.content.text_content import FILTERS_MESSAGE

    
@dp.message(
    lambda message: len(message.text) > 20,
    AddPost.title
)
async def repeat_enter_title(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['create_post']['repeat_title'])

@dp.message(
    lambda message: len(message.text) < 20,
    AddPost.text
)
async def repeat_enter_text(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['create_post']['repeat_text'])

@dp.message(
    lambda message: message.text not in [button[0]['text'] for button in direction_detection_buttons['keyboard']],
    AddPost.direction
)
async def repeat_enter_direction(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['create_post']['repeat_direction'])