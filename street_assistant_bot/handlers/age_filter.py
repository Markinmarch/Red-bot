from aiogram import types

from street_assistant_bot.misc import dp
from street_assistant_bot.states import Form


# Check age. Age gotta be digit
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def process_age_invalid(message: types.Message):
    return await message.reply('Мне необходимы цифры.\nВведите Ваш возраст (только цифрами)')
