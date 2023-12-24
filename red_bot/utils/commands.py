from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands_for_users(bot: Bot):
    menu_commands = [
        BotCommand(
            command = 'delete_account',
            description = 'Удалить учётную запись'
        ),
        BotCommand(
            command = 'create_post',
            description = 'Создать запись на канале'
        ),
        BotCommand(
            command = 'my_posts',
            description = 'Список моих записей'
        ),
        BotCommand(
            command = 'rules',
            description = 'Правила пользования телеграм-каналом'
        ),
        BotCommand(
            command = 'contact',
            description = 'Связь с администрацией канала'
        )
    ]

    await bot.set_my_commands(
        commands = menu_commands,
        scope = BotCommandScopeDefault()
    )