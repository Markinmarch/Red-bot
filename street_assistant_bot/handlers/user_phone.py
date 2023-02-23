from aiogram import types
from aiogram.dispatcher import FSMContext

from street_assistant_bot.misc import dp
from street_assistant_bot.states import Form


@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

    await message.answer(
        text = '<p>Введите Ваш номер телефона <i>(начиная с 8, например 89781234567)</i></p>',
        parse_mode= 'HTML'
    )
    await Form.next()