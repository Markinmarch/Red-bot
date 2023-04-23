from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser


@dp.callback_query_handler(text = 'agree')
async def cmd_start_registration(callback: types.CallbackQuery):
    # инициализируем State()
    await AddUser.name.set()
    # и спрашивем имя нового пользователя
    await callback.message.answer(
        text ='Введите Ваше имя'
    )    
