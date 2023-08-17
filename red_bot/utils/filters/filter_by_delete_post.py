from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.state import DeletePost
from red_bot.utils.content.text_content import FILTERS_MESSAGE


@dp.message_handler(
    lambda message: message.text.isdigit() is False,
    state = DeletePost.num_post
)
async def check_age(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['delete_post'])
