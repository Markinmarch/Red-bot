from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser
from red_bot.utils.keyboards.replay_keyboard import get_phone_user


@dp.message_handler(state = AddUser.gender)
async def add_gender__cmd_phone(message: types.Message, state: FSMContext):
    '''
    Данный объект записывает в состояние State()
    пол нового пользователя и переходит к следующему
    состоянию, запрашивающему разрешение на получение
    контактных данных пользователя (телефон аккаунта)
    -----------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) пола пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''    
    # записываем пол пользователя
    await state.update_data(gender = message.text)
    
    # переходим к следуюшему стейту и спрашиваем номер телефона
    await AddUser.next()
    await message.answer(
        'Согласны дать нам свой номер телефона?',
        reply_markup = get_phone_user
    )
