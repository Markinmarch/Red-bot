from aiogram import types

from street_assistant_bot.misc import dp
from street_assistant_bot.states import Form


@dp.message_handler(commands='start')
async def cmd_start(msg: types.Message): 
    await msg.answer(
        text = '<p>Для корректной коммуникации с сервисами и магазинами введите <b>корректное имя</b></p>',
        parse_mode='HTML'
    )
    await Form.name.set()
