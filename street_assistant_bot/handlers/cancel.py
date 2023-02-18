from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from street_assistant_bot.misc import dp, logger


# Не уверен что state='*' обязателен, мне кажется что так по дефолту стоит
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True))
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logger.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Отменено.', reply_markup=types.ReplyKeyboardRemove())