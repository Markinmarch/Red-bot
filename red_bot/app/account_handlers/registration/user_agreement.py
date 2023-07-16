from aiogram import types


from red_bot.settings.setting import dp
from red_bot.utils.content.text_content import WELCOME
from red_bot.utils.keyboards.inline_keyboard import agree_button


@dp.callback_query_handler(text = 'create_account')
async def user_agreement_via_query(callback: types.CallbackQuery) -> None:
    '''
    Данный объект реализует получение согласия от пользователя
    на дальнейшую регистрацию через запрос (нажатие кнопки)
    ----------------------------------------------------------
    parametrs:
        :text: фильтр обратного вызова обработчика
        :callback: тип объекта представления
    '''
    await callback.message.answer(
        text = WELCOME,
        parse_mode = 'HTML',
        reply_markup = agree_button
    )

@dp.message_handler(commands = ['create_account'])
async def user_agreement_via_command(message: types.Message) -> None:
    '''
    Данный объект реализует получение согласия от пользователя
    на дальнейшую регистрацию через команду
    ----------------------------------------------------------
    parametrs:
        :commands: команда, закреплённая за обработчиком
        :message: тип объекта представления
    '''
    welcome_message = await message.answer(
        text = WELCOME,
        parse_mode = 'HTML',
        reply_markup = agree_button
    )
