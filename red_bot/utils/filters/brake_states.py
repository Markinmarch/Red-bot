from aiogram import types, F
from aiogram.fsm.context import FSMContext


from red_bot.settings.setting import dp
from red_bot.utils.content.text_content import FILTERS_MESSAGE
from red_bot.utils.state import AddPost, AddUser, DeletePost

@dp.message(
    F.text == 'Отменить ❌',
    state = AddUser.__all_states__
)
async def brake_state_AddUser(
    message: types.Message,
    state: FSMContext
):
    await message.answer(
        text = FILTERS_MESSAGE['command_brake'],
        reply_markup = types.ReplyKeyboardRemove()
        )
    await state.clear()

@dp.message(
    F.text == 'Отменить ❌',
    state = AddPost.__all_states__
)
async def brake_state_AddPost(
    message: types.Message,
    state: FSMContext
):
    await message.answer(
        text = FILTERS_MESSAGE['command_brake'],
        reply_markup = types.ReplyKeyboardRemove()
        )
    await state.clear()

@dp.message_handler(
    F.text == 'Отменить ❌',
    state = DeletePost.__all_states__
)
async def brake_state_DeletePost(
    message: types.Message,
    state: FSMContext
):
    await message.answer(
        text = FILTERS_MESSAGE['command_brake'],
        reply_markup = types.ReplyKeyboardRemove()
        )
    await state.clear()