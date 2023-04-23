from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser


@dp.message_handler(state = AddUser.age)
async def add_age__cmd_gender(message: types.Message, state: FSMContext):
    # записываем возраст пользователя
    if message.text.isdigit():
        await state.update_data(age = int(message.text))
    else:
        await message.answer('Необходимы только цифры! Введите Ваш возраст')
        
    # переходим к следуюшему стейту и спрашиваем про пол
    await AddUser.next()
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True, selective = True)
    markup.add('Мужской', 'Женский')
    await message.reply(
        'Укажите свой пол',
        reply_markup = markup
    )