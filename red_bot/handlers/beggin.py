from aiogram import types


from red_bot.settings.setting import dp


@dp.message_handler(commands = ['start', 'help'])
async def condition_of_agree(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    registration_btn = types.KeyboardButton(text = '📝 Регистрация')
    markup.add(registration_btn)
    await message.answer(
        text = 'Привет! Я бот, который поможет Вам найти быструю работу или разместить своё объявление с предложением.\n'
        'Но для начала Вам необходимо ознакомиться с некоторыми правилами и юридическими аспектами, чтобы не стать жертвой мошенников.\n'
        'Для этого перейди по <b><a href = "https://telegra.ph/Pravila-polzovaniya-telegram-botom-02-25">ссылке</a></b> и прочти обязательно правила!\n'
        'Ваша дальнейшая регистрация автоматически подтверждает, что Вы ознакомились с правилами.',
        parse_mode = 'HTML',
        reply_markup = markup
    )