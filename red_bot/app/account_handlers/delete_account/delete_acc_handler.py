from aiogram import types
import logging


from red_bot.settings.setting import dp
from red_bot.utils.keyboards.inline_keyboard import delete_acc_button
from red_bot.utils.commands import set_commands_for_new_user
from red_bot.sql_db import db


@dp.message_handler(commands = ['delete_account'])
async def delete_account(message: types.Message):
    await message.answer(
        text = 'Если Вы удалите свой аккаунт, то и все Ваши записи с канала будут удалены. У Вас больше не будет возможности создавать посты, но Вы по прежнему сможете отзываться на них.',
        parse_mode = 'HTML',
        reply_markup = delete_acc_button
    )

@dp.callback_query_handler(text = 'delete_account')
async def erase_user_data(callback: types.CallbackQuery):
    await set_commands_for_new_user(bot = callback.bot)
    try:
        if callback.from_user.id in db.users_database.ids_users():
            db.users_database.delete_users(user_id = callback.from_user.id)
            await callback.answer(
                text = 'Ваш аккаунт удалён',
                show_alert = True
            )
            logging.info(f'User {callback.from_user.id} has been deleted')
        else:
            await callback.answer(
                text = 'Ваш аккаунт уже удалён',
                show_alert = True
            )
    except TypeError:
        await callback.answer(
            text = 'Ваш аккаунт уже удалён',
            show_alert = True
        )
