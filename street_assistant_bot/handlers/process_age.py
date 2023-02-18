from aiogram import types
from aiogram.dispatcher import FSMContext

from street_assistant_bot.misc import dp
from street_assistant_bot.states import Form


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    # Update state and data
    await Form.next()
    await state.update_data(age=int(message.text))

    # Configure ReplyKeyboardMarkup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add('Муж.', 'Жен.')

    await message.reply('Укажите Ваш пол', reply_markup=markup)
