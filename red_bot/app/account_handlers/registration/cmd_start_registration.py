from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser


@dp.callback_query_handler(text = 'user_agree')
async def cmd_start_registration(callback: types.CallbackQuery) -> None:
    '''
    Данный объект инициализирует состояние State()
    и запрашивает имя нового пользователя
    -----------------------------------------------
    parametrs:
        :text: фильтр обратного вызова обработчика
        :callback: тип объекта представления
    '''
    # инициализируем State()
    await AddUser.name.set()
    # и спрашивем имя нового пользователя
    await callback.message.answer(
        text ='Введите Ваше имя'
    )    
