from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddRecord


@dp.message_handler(state = AddRecord.conditions)
async def add_conditions__cmd_photo(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as user_data:
        user_data['conditions'] = message.text
        
    # переходим к следуюшему стейту и спрашиваем про возраст
    await AddRecord.next()
    await message.answer('Можете прикрепть до двух трёх фотографий по желанию')