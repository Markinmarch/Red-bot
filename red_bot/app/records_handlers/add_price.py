from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddRecord


@dp.message_handler(state = AddRecord.price)
async def add_photo__cmd_price(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as user_data:
        user_data['price'] = message.text
        
    # переходим к следуюшему стейту и спрашиваем про возраст
    await AddRecord.next()
    await message.answer('Укажите цену за работу/услугу/товар/сырьё (напр. 300 руб/час; 800 руб/куб')

    await state.finish()