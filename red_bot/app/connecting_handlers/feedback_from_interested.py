from aiogram import types


from red_bot.settings.setting import dp, bot



@dp.callback_query_handler(text = 'respond_to_ad')
async def feedback_user(callback: types.CallbackQuery):
    await callback.answer(
        text = 'Отзыв отправлен',
        show_alert = True
    )

    # await callback.answer(
    #     chat_id = callback.forward_from.id,
    #     text = 'Хелёу!'
    # )
    # await print(callback.bot.copy_message(chat_id=callback.from_user.id, from_chat_id=3461209012101529925, message_id=5418234913691564248))s
    # await callback.bot.forward_message(
    #     chat_id = callback.from_user.id,
    #     from_chat_id = callback.message.from_id,
    #     message_id = callback.message.message_id,
    #     message_thread_id = callback.message.forward_sender_name
    # )
    # await callback.bot.get_chat(
    #     chat_id=callback.from_user.id
    # )

