from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.content import POST_INSTRUCTION
from red_bot.utils.keyboards.inline_keyboard import continue_filling_button


@dp.message_handler(commands=['create_post'])
async def user_rules_reminder(message: types.Message):
    await message.answer(
        text = POST_INSTRUCTION,
        parse_mode = 'HTML',
        reply_markup = continue_filling_button
    )
