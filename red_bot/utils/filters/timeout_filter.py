from aiogram import types
from async_timeout import timeout


from red_bot.settings.setting import dp


@dp.message_handler(commands = ['start', 'create_account'])
async def registration_timeout(message: types.Message):
    pass