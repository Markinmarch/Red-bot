from aiogram import types


from red_bot.settings.setting import bot, dp
from red_bot.utils.state import AddUser


@dp.message_handler(
    lambda message: message.text.isalpha() is False,
    state = AddUser.name
)
async def check_name(message: types.Message):
    await message.answer(text = 'Пожалуйста, повторите попытку. В псевдониме не должно быть никаких цифр и других символов. Только буквы кириллицей.')

@dp.message_handler(
    lambda message: message.text.isdigit() is False,
    state = AddUser.age
)
async def check_age(message: types.Message):
    await message.answer(text = 'Пожалуйста, укажите возраст только цифрами.')

@dp.message_handler(
    lambda message: message.text not in ['Мужской', 'Женский'],
    state = AddUser.gender
)
async def check_gender(message: types.Message):
    await message.answer(text = 'Пожалуйста, выберите один из двух вариантов.')
    