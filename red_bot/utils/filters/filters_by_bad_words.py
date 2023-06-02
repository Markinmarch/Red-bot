from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.content.text_content import BAD_WORDS

@dp.message_handler(lambda message: message in BAD_WORDS)
async def block_bad_words(message: types.Message):
    await message.answer(
        text = 'Пожалуйста, не используйте ненормативную лексику. Помните о <b><a href = "https://telegra.ph/Pravila-polzovaniya-telegram-botom-02-25">правилах</a></b> пользования каналом!',
        parse_mode = 'HTML'
    )
