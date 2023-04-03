from aiogram import types


from red_bot.settings.setting import dp
from red_bot.settings.state import AddUser
# from red_bot.sql_db.db import database as db


@dp.message_handler(text = '📝 Регистрация')
async def cmd_name(message: types.Message):
    # инициализируем State()
    await AddUser.name.set()
    # и спрашивем имя нового пользователя
    await message.answer(
        'Введите Ваше имя',
        reply_markup = types.ReplyKeyboardRemove()
    )    
    

# @dp.message_handler(content_types = ['text'])
# async def add_age(message: types.Message):
#     # запаршиваем у пользователя возраст
#     await AddUser.age.set()
#     await message.reply('Укажите Ваш возраст (только цифрами)')
#     return message.text.isdigit()


    # # запрашиваем у пользователя возраст
    # await message.answer('Введите Ваш возраст (цифрами)')
    # user_age = message.text.isdigit()
    # await AddUser.next()

    # # запрашиваем у пользователя пол
    # markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    # markup.add('Мужской', 'Женский')
    # await message.answer(
    #     'Выберите свой пол',
    #     reply_markup = markup 
    # )
    # if message.text == 'Мужской':
    #     user_gender = 1
    # if message.text == 'Женский':
    #     user_gender = 0
    # await AddUser.next()

    # # запрашиваем у пользователя номер телефона
    # await AddUser.next()
    # await message.answer(
    #     'Введите свой рабочий номер телефона',
    #     reply_markup = types.ReplyKeyboardRemove()
    # )
    # user_phone = message.text.isdigit()

    # await db.insert_users(
    #     message.from_user.id,
    #     user_name,
    #     user_age,
    #     user_gender,
    #     user_phone
    # )
    # await db.conn.commit()
    # await db.conn.close()

    # await state.finish()

        # async with context.proxy() as user_data:
        #     user_data['name'] = message.text
        
        #     # запрашиваем у пользователя возраст
        #     await AddUser.next()
        #     await message.reply('Введите Ваш возраст (цифрами)')
        #     user_data['age'] = message.text.isdigit()

        #     # запрашиваем у пользователя пол
        #     await AddUser.next()
        #     markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        #     markup.add('Мужской', 'Женский')
        #     await message.reply(
        #         'Выберите свой пол',
        #         reply_markup = markup 
        #     )
        #     if message.text == 'Мужской':
        #         user_data['gender'] = 1
        #     else:
        #         user_data['gender'] = 0

        #     # запрашиваем у пользователя номер телефона
        #     await AddUser.next()
        #     await message.reply(
        #         'Введите свой рабочий номер телефона',
        #         reply_markup = types.ReplyKeyboardRemove()
        #     )
        #     user_data['phone'] = message.text.isdigit()

        #     db.insert_users(
        #         message.from_user.id,
        #         user_data['name'],
        #         user_data['age'],
        #         user_data['gender'],
        #         user_data['phone']
        #     )
        #     db.conn.commit()
        #     db.conn.close()

        # await context.finish()

        # await message.answer(
        #     text = 'Готово!'
        # )
