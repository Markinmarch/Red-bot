from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser
from red_bot.utils.keyboards.replay_keyboard import get_phone_user


@dp.message_handler(state = AddUser.gender)
async def add_gender__cmd_phone(message: types.Message, state: FSMContext):
    # записываем пол пользователя
    await state.update_data(gender = message.text)
    
    # переходим к следуюшему стейту и спрашиваем номер телефона
    await AddUser.next()
    await message.answer(
        'Согласны дать нам свой номер телефона?',
        reply_markup = get_phone_user
    )