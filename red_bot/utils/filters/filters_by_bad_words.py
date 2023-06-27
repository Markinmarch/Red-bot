from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.content.text_content import BAD_WORDS
from red_bot.utils.state import AddPost, AddUser

@dp.message_handler(
    lambda message: message.text in BAD_WORDS,
    state = AddUser.all_states
)
async def block_bad_words_in_registration(message: types.Message):
    await message.answer(
        text = 'Пожалуйста, не используйте ненормативную лексику. Помните о <b><a href = "https://telegra.ph/Pravila-polzovaniya-telegram-botom-02-25">правилах</a></b> пользования каналом!',
        parse_mode = 'HTML'
    )

@dp.message_handler(
    lambda message: message.text in BAD_WORDS,
    state = AddPost.all_states
)
async def block_bad_words_in_posts(message: types.Message):
    await message.answer(
        text = 'Пожалуйста, не используйте ненормативную лексику. Помните о <b><a href = "https://telegra.ph/Pravila-polzovaniya-telegram-botom-02-25">правилах</a></b> пользования каналом!',
        parse_mode = 'HTML'
    )
