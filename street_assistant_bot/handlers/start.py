from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from street_assistant_bot.misc import dp
from street_assistant_bot.states import Form


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await Form.name.set()
    await message.answer('Для корректной коммуникации с сервисами и магазинами введите корректное имя')
