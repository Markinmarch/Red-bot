from aiogram import types
from aiogram.dispatcher import FSMContext
import asyncio


from red_bot.settings.setting import dp
from red_bot.utils.state import AddUser
from red_bot.utils.content.text_content import INTERRUPTION_MESSAGE, REGISTRATION_MESSAGE


@dp.callback_query_handler(text = 'user_agree')
async def cmd_start_registration(callback: types.CallbackQuery, state: FSMContext) -> None:
    '''
    Данный объект инициализирует состояние State()
    и запрашивает имя нового пользователя
    -----------------------------------------------
    parametrs:
        :text: фильтр обратного вызова обработчика
        :callback: тип объекта представления
    '''
    await AddUser.name.set()
    await callback.message.answer(text = REGISTRATION_MESSAGE['add_name'])    
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(12)
    try:
        data = await state.get_data()
        if data['name'] != None:
            pass
    except KeyError:
        await callback.message.answer(text = INTERRUPTION_MESSAGE)
        await state.finish()
    
