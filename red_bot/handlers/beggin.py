from aiogram import types
from aiogram.dispatcher.filters import CommandStart


from red_bot.settings.setting import dp
from red_bot.settings.state import AddUser


@dp.message_handler(commands = ['start', 'help'])
async def cmd_beggin(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    registration_btn = types.KeyboardButton(text = '📝 Регистрация')
    exit_btn = types.KeyboardButton('🙅‍♂️ Выход')
    markup.add(registration_btn, exit_btn)
    await message.answer(
        message.chat.id,
        text = 'Привет! Я бот, который поможет тебе найти быструю работу или разместить своё объявление с предложением.\n'
        'Но для начала тебе необходимо ознакомиться с некоторыми правилами и юридическими аспектами, чтобы не стать жертвой мошенников.\n'
        'Для этого перейди по <b><a href = "https://telegra.ph/Pravila-polzovaniya-telegram-botom-02-25">ссылке</a></b> и прочти обязательно правила!\n'
        'Ваша дальнейшая регистрация автоматически подтверждает, что Вы ознакомились с правилами.',
        parse_mode = 'HTML',
        reply_markup = markup
    )