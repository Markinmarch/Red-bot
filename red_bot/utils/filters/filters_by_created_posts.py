from aiogram import types, F


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost
from red_bot.utils.content.text_content import FILTERS_MESSAGE

    
@dp.message(
    len(F.text) > 20,
    state = AddPost.title
)
async def repeat_enter_title(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['create_post']['repeat_title'])

@dp.message(
    len(F.text) < 20,
    state = AddPost.text
)
async def repeat_enter_text(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['create_post']['repeat_text'])

# @dp.message(
#     lambda message: message.text not in [button[0]['text'] for button in direction_detection_buttons['keyboard']],
#     state = AddPost.direction
# )
# async def repeat_enter_direction(message: types.Message):
#     await message.answer(text = FILTERS_MESSAGE['create_post']['repeat_direction'])