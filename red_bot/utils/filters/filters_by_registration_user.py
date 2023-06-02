from aiogram import types


from red_bot.settings.setting import dp
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

@dp.message_handler(
    lambda message: message.text.isdigit() is False and len(message.text) != 11,
    state = AddUser.phone
)
async def check_phone(message: types.Message):
    await message.answer(text = 'Пожалуйста, убедитесь, что верно ввели свой номер телефона и попробуйте ещё раз. Начинайти вводить номер телефона с цифры "8"')