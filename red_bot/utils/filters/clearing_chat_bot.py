from aiogram import types
from asyncio import sleep
import logging


from red_bot.settings.setting import dp


@dp.callback_query_handler(text = 'publish')
async def clearing_chat_bot(callback: types.CallbackQuery):
    sleep(15)
    msg_id = callback.message.message_id
    while callback.message.text != None:
        await callback.message.bot.delete_message(
            chat_id = callback.message.chat.id,
            message_id = msg_id
        )
        msg_id -= 1
        break
    logging.info(f'Chat with user {callback.from_user.full_name} has been clearing')
