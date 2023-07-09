from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost


@dp.message_handler(state = AddPost.title)
async def add_title__cmd_text(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as from_user_data:
        from_user_data['title'] = message.text
        
    # переходим к следуюшему стейту и спрашиваем про возраст
    await AddPost.next()
    await message.answer('Напишите содержание записи с подробностями')