from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser
from red_bot.utils.keyboards.reply_keyboard import choose_gender
from red_bot.utils.content.text_content import FILTERS_MESSAGE


@dp.message(
    lambda message: message.text.isalpha() is False,
    AddUser.name
)
async def check_name(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['registration_user']['name_filter'])

@dp.message(
    lambda message: message.text.isdigit() is False,
    AddUser.age
)
async def check_age(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['registration_user']['age_filter'])

@dp.message(
    lambda message: message.text not in [button[0]['text'] for button in choose_gender['keyboard']],
    AddUser.gender
)
async def check_gender(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['registration_user']['gender_filter'])
