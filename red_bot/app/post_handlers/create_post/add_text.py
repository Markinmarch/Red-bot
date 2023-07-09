from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.state import AddPost
from red_bot.utils.keyboards.replay_keyboard import by_agreement


@dp.message_handler(state = AddPost.text)
async def add_text__cmd_conditions(message: types.Message, state: FSMContext):
    # записываем имя пользователя
    async with state.proxy() as from_user_data:
        from_user_data['text'] = message.text
        
    # переходим к следуюшему стейту и спрашиваем про возраст
    await AddPost.next()
    await message.answer(
        text = 'Опишите условия работы - зарплату/цену за заказ',
        reply_markup = by_agreement
    )