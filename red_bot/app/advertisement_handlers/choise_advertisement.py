from aiogram import types


from red_bot.settings.setting import dp


@dp.callback_query_handler(text = 'authorization')
async def authorization_old_user(callback: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    jobs_btn = types.InlineKeyboardButton(text = 'Работа', callback_data = 'jobs')
    services_btn = types.InlineKeyboardButton(text = 'Услуги', callback_data = 'services')
    offers_btn = types.InlineKeyboardButton(text = 'Предложения', callback_data = 'offers')
    exchanges_btn = types.InlineKeyboardButton(text = 'Биржа', callback_data = 'exchanges')
    markup.add(
        jobs_btn,
        services_btn,
        offers_btn,
        exchanges_btn
    )
    await callback.answer(text = 'Подождите, проходит авторизация.')
    await callback.message.answer(text = 'Выберите направление', reply_markup = markup)
