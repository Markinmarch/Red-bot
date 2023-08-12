from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser
from red_bot.utils.keyboards.reply_keyboard import choose_gender
from red_bot.utils.content.text_content import REGISTRATION_FILTER


@dp.message_handler(
    lambda message: message.text.isalpha() is False,
    state = AddUser.name
)
async def check_name(message: types.Message):
    await message.answer(text = REGISTRATION_FILTER['name_filter'])

@dp.message_handler(
    lambda message: message.text.isdigit() is False,
    state = AddUser.age
)
async def check_age(message: types.Message):
    await message.answer(text = REGISTRATION_FILTER['age_filter'])

@dp.message_handler(
    lambda message: message.text not in [key[0]['text'] for key in choose_gender['keyboard']],
    state = AddUser.gender
)
async def check_gender(message: types.Message):
    await message.answer(text = REGISTRATION_FILTER['gender_filter'])
