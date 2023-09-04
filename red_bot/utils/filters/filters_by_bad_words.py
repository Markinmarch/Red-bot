from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.content.text_content import BAD_WORDS, FILTERS_MESSAGE
from red_bot.utils.state import AddPost, AddUser

@dp.message(
    lambda message: message.text in BAD_WORDS,
    AddUser.__all_states__
)
async def block_bad_words_in_registration(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['bad_words'])

@dp.message(
    lambda message: message.text in BAD_WORDS,
    state = AddPost.__all_states__
)
async def block_bad_words_in_posts(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['bad_words'])
