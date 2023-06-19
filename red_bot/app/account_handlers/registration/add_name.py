from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser


@dp.message_handler(state = AddUser.name)
async def add_name__cmd_age(message: types.Message, state: FSMContext) -> None:
    '''
    Данный объект записывает в состояние State()
    имя нового пользователя и переходит к следующему
    состоянию, запрашивающему возраст пользователя
    -----------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) имени пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''
    # записываем имя пользователя
    async with state.proxy() as user_data:
        user_data['name'] = message.text
        
    # переходим к следуюшему стейту и спрашиваем про возраст
    await AddUser.next()
    await message.answer('Укажите Ваш возраст (только цифрами)')