from aiogram import types, F
from aiogram.filters import Command


from ...settings.setting import dp
from ...settings.config import RULES_URL


@dp.message(Command('rules'))
async def get_rules(message: types.Message) -> None:
    '''
    Данный объект реализует перенаправление пользователя по ссылке
    с правилами телеграм-канала.
    ----------------------------------------------------------
    parametrs:
        :commands: команда вызова обработчика
        :message: тип объекта представления
    '''
    await message.answer(
        text = RULES_URL
    )