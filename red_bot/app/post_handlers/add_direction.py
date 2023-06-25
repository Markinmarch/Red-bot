from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost


@dp.message_handler(state = AddPost.direction)
async def add_direction__cmd_title(message: types.Message, state: FSMContext):
    # записываем направление выбранное пользователем
    async with state.proxy() as from_user_data:
        from_user_data['direction'] = message.text
        
    # переходим к следуюшему стейту и просим ввести описание
    await AddPost.next()
    await message.answer(
        text = 'Напишите краткое описание записи (напр. Подработка/Услуги сантехника/Дрова/Уголь/Вывезти мусор)',
        reply_markup = types.ReplyKeyboardRemove()
    )