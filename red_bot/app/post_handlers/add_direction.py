from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddRecord


@dp.message_handler(state = AddRecord.direction)
async def add_direction__cmd_title(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as from_user_data:
        from_user_data['direction'] = message.text
        
    # переходим к следуюшему стейту и спрашиваем про возраст
    await AddRecord.next()
    await message.answer(
        text = 'Напишите краткое описание записи (напр. Подработка/Услуги сантехника/Дрова/Уголь/Вывезти мусор)',
        reply_markup = types.ReplyKeyboardRemove()
    )