from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.settings.state import AddUser


@dp.message_handler(state = AddUser.gender)
async def add_gender__cmd_phone(message: types.Message, state: FSMContext):
    # записываем пол пользователя
    await state.update_data(gender = message.text)
    
    # переходим к следуюшему стейту и спрашиваем номер телефона
    await AddUser.next()
    await message.reply(
        'Укажите Ваш рабочий номер телефона',
        reply_markup = types.ReplyKeyboardRemove()
    )