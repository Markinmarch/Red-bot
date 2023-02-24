from aiogram import types
from aiogram.dispatcher import FSMContext

from street_assistant_bot.misc import dp
from street_assistant_bot.states import Form


@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
    await message.reply('Введите Ваш возраст')