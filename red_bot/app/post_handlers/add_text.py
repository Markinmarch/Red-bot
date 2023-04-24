from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddRecord


@dp.message_handler(state = AddRecord.text)
async def add_text__cmd_conditions(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as user_data:
        user_data['text'] = message.text
        
    # переходим к следуюшему стейту и спрашиваем про возраст
    await AddRecord.next()
    await message.answer('Опишите условия работы - зарплату/цену за заказ')