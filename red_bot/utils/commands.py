from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    menu_commands = [
        BotCommand(
            command = 'create_account',
            description = 'Создать учётную запись'
        ),
        BotCommand(
            command = 'delete_account',
            description = 'Удалить учётную запись'
        ),
        BotCommand(
            command = 'create_record',
            description = 'Создать запись на канале'
        ),
        BotCommand(
            command = 'my_records',
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