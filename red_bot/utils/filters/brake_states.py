from aiogram import types, F
from aiogram.fsm.context import FSMContext


from ...settings.setting import dp
from ..content.text_content import FILTERS_MESSAGE


@dp.message(F.text == 'Отменить ❌')
async def brake(
    message: types.Message,
    state: FSMContext
):
    await message.answer(
        text = FILTERS_MESSAGE['command_brake'],
        reply_markup = types.ReplyKeyboardRemove()
        )
    await state.clear()