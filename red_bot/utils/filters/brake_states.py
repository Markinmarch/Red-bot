from aiogram import types
from aiogram.dispatcher import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.content.text_content import FILTERS_MESSAGE
from red_bot.utils.state import AddPost, AddUser, DeletePost

@dp.message_handler(
    lambda message: message.text == 'Отменить ❌',
    state = AddUser.all_states
)
async def brake_state_AddUser(
    message: types.Message,
    state: FSMContext
):
    await message.answer(
        text = FILTERS_MESSAGE['command_brake'],
        reply_markup = types.ReplyKeyboardRemove()
        )
    await state.finish()

@dp.message_handler(
    lambda message: message.text == 'Отменить ❌',
    state = AddPost.all_states
)
async def brake_state_AddPost(
    message: types.Message,
    state: FSMContext
):
    await message.answer(
        text = FILTERS_MESSAGE['command_brake'],
        reply_markup = types.ReplyKeyboardRemove()
        )
    await state.finish()

@dp.message_handler(
    lambda message: message.text == 'Отменить ❌',
    state = DeletePost.all_states
)
async def brake_state_DeletePost(
    message: types.Message,
    state: FSMContext
):
    await message.answer(
        text = FILTERS_MESSAGE['command_brake'],
        reply_markup = types.ReplyKeyboardRemove()
        )
    await state.finish()