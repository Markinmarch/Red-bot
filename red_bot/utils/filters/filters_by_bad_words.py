from aiogram import types, F


from ...settings.setting import dp
from ..content.text_content import BAD_WORDS, FILTERS_MESSAGE
from ..state import AddPost


@dp.message(AddPost.__all_states__)
async def block_bad_words_in_posts(message: types.Message):
    for bad_word in BAD_WORDS:
        if bad_word in F.text:
            await message.answer(text = FILTERS_MESSAGE['bad_words'])
