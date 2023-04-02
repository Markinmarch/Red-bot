from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.settings.state import AddUser


@dp.message_handler(state = AddUser.name)
async def add_name__cmd_age(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as user_data:
        user_data['name'] = message.text
        
    # переходим к следуюшему стейту и спрашиваем про возраст
    await AddUser.next()
    await message.reply('Укажите Ваш возраст (только цифрами)')