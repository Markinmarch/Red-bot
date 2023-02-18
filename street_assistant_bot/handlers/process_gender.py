from aiogram import types
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as md

from street_assistant_bot.misc import dp, bot
from street_assistant_bot.states import Form


@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

        # Remove keyboard
        markup = types.ReplyKeyboardRemove()

        # And send message
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Спасибо', md.bold(data['name'])),
                md.text('Теперь мы можем приступать!'),
                sep='\n',
            ),
            reply_markup=markup,
            parse_mode=types.ParseMode.MARKDOWN,
        )

    # Finish conversation
    await state.finish()