from hot_offer_bot.core.settings import bot
from telebot import types
from hot_offer_bot.DB.db_map import database as db


@bot.message_handler(content_types = ['text'])
async def choise_user(message: types.Message):

    if (message.text == '📝 Регистрация'):
        await bot.send_message(
            chat_id = message.chat.id,
            text = 'Отлично! Тогда приступим!',
            reply_markup = types.ReplyKeyboardRemove()
        )

    if (message.text == '🙅‍♂️ Выход'):
        await bot.send_message(
            chat_id = message.chat.id,
            text = 'Возможно позже Вы найдёте что-то интересное у нас, заходите ещё! Будем жадть!',
            reply_markup = types.ReplyKeyboardRemove()
        )

@bot.message_handler(commands = ['registration'])
async def register_user(message: types.Message):
    await bot.send_message(
        message.chat.id,
        text = 'А-ху-еть!'
    )