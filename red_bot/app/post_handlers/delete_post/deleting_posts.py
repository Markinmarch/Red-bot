# from aiogram import types
# import logging


# from red_bot.settings.config import CHANNEL_ID
# from red_bot.settings.setting import dp
# from red_bot.utils.keyboards.inline_keyboard import delete_acc_button
# from red_bot.utils.commands import set_commands_for_new_user
# from red_bot.sql_db import posts_db, users_db
# from red_bot.utils.content.text_content import DELETE_ACCOUNT_MESSAGE, BEFORE_DEL_ACC_MESSAGE

# @dp.callback_query_handler(text = 'delete_post')
# async def erase_user_data(callback: types.CallbackQuery):
#     await callback.bot.delete_message(
#         chat_id = CHANNEL_ID,
#         message_id = num_post
#     )
#     posts_db.posts.delete_posts(num_post)