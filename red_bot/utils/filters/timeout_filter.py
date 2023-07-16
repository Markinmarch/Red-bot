import asyncio
from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser


@dp.message_handler(
    lambda message: message == None,
    state = AddUser.all_states
)
async def timeout_filter(message: types.Message):
    message.bot.request_timeout(5)
