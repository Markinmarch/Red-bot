from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddRecord


@dp.message_handler(state = AddRecord.photo, content_types = [types.ContentType.PHOTO, types.ContentType.TEXT])
async def add_photo__cmd_price(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as user_data:
        user_data['photo'] = message.text
        
    # переходим к следуюшему стейту и спрашиваем про возраст
    await AddRecord.next()
    await message.answer('Укажите цену за работу/услугу/товар/сырьё')