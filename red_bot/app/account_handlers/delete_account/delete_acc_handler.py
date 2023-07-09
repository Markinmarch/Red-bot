from aiogram import types
import logging


from red_bot.settings.setting import dp
from red_bot.utils.keyboards.inline_keyboard import delete_acc_button
from red_bot.utils.commands import set_commands_for_new_user
from red_bot.sql_db.users import users
from red_bot.utils.content.text_content import DELETE_ACCOUNT_MESSAGE, BEFORE_DEL_ACC_MESSAGE


@dp.message_handler(commands = ['delete_account'])
async def delete_account(message: types.Message):
    await message.answer(
        text = BEFORE_DEL_ACC_MESSAGE,
        parse_mode = 'HTML',
        reply_markup = delete_acc_button
    )

@dp.callback_query_handler(text = 'delete_account')
async def erase_user_data(callback: types.CallbackQuery):
    if users.checking_users(callback.from_user.id) == True:
        users.delete_users(user_id = callback.from_user.id)
        await set_commands_for_new_user(bot = callback.bot)
        await callback.answer(
            text = DELETE_ACCOUNT_MESSAGE,
            show_alert = True
        )
        logging.info(f'User {callback.from_user.id} has been deleted')
    else:
        await callback.answer(
            text = DELETE_ACCOUNT_MESSAGE,
            show_alert = True
        )
