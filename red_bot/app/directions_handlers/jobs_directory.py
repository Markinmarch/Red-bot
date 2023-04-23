from aiogram import types


from red_bot.settings.setting import dp


@dp.callback_query_handler(text = 'jobs')
async def jobs_directory(callback: types.CallbackQuery):
    pass