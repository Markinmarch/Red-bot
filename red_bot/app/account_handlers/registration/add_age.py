from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser
from red_bot.utils.keyboards.replay_keyboard import choose_gender


@dp.message_handler(state = AddUser.age)
async def add_age__cmd_gender(message: types.Message, state: FSMContext):
    '''
    Данный объект записывает в состояние State()
    возраст нового пользователя и переходит к следующему
    состоянию, запрашивающему пол пользователя
    -----------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) телефона пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''    
    # записываем возраст пользователя
    if message.text.isdigit():
        await state.update_data(age = int(message.text))
    else:
        await message.answer('Необходимы только цифры! Введите Ваш возраст')
        
    # переходим к следуюшему стейту и спрашиваем про пол
    await AddUser.next()
    await message.reply(
        'Укажите свой пол',
        reply_markup = choose_gender
    )