from aiogram import types


from red_bot.settings.setting import dp
from red_bot.settings.state import AddUser


@dp.message_handler(text = '📝 Регистрация')
async def cmd_registration(message: types.Message):
    # инициализируем State()
    await AddUser.name.set()
    # и спрашивем имя нового пользователя
    await message.answer(
        'Введите Ваше имя',
        reply_markup = types.ReplyKeyboardRemove()
    )    
