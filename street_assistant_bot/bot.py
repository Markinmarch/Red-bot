# import logging
# from street_assistant_bot.config import BOT_TOKEN

# import aiogram.utils.markdown as md

# from aiogram.dispatcher.filters import Text

# from aiogram.types import ParseMode
# from aiogram.utils import executor

# @dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
# async def process_age(message: types.Message, state: FSMContext):
#     # Update state and data
#     await Form.next()
#     await state.update_data(age=int(message.text))

#     # Configure ReplyKeyboardMarkup
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
#     markup.add('Муж.', 'Жен.')

#     await message.reply('Укажите Ваш пол', reply_markup=markup)


# @dp.message_handler(state=Form.gender)
# async def process_gender(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['gender'] = message.text

#         # Remove keyboard
#         markup = types.ReplyKeyboardRemove()

#         # And send message
#         await bot.send_message(
#             message.chat.id,
#             md.text(
#                 md.text('Hi! Nice to meet you,', md.bold(data['name'])),
#                 md.text('Age:', md.code(data['age'])),
#                 md.text('Gender:', data['gender']),
#                 sep='\n',
#             ),
#             reply_markup=markup,
#             parse_mode=ParseMode.MARKDOWN,
#         )

#     # Finish conversation
#     await state.finish()


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)