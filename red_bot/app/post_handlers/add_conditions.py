from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddRecord
from red_bot.utils.keyboards.replay_keyboard import continue_publishing


@dp.message_handler(state = AddRecord.conditions)
async def add_conditions__cmd_photo(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as from_user_data:
        from_user_data['conditions'] = message.text

    # переходим к следуюшему стейту и спрашиваем про возраст
    await AddRecord.next()
    await message.answer(
        text = 'Можете прикрепить одну фотографию к записи по желанию либо опубликовать свою запись сразу',
        reply_markup = continue_publishing
    )