from aiogram import types
from aiogram.dispatcher import FSMContext

from street_assistant_bot.misc import dp
from street_assistant_bot.states import Form


@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

    await Form.next()
    await message.answer('Введите Ваш номер телефона (начиная с 8, например 89781234567)')