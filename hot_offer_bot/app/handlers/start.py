from hot_offer_bot.core.settings import bot
from telebot import types
from telebot.callback_data import CallbackData


@bot.message_handler(commands = ['help', 'start'])
async def send_welcom(message: types.Message):
    register_command = CallbackData('registration', prefix = 'qwerty')
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    registration_btn = types.InlineKeyboardButton(text = '📝 Регистрация', callback_data = register_command.new(function = 'add_user'))
    exit_btn = types.InlineKeyboardButton('🙅‍♂️ Выход')
    markup.add(registration_btn, exit_btn)
    await bot.send_message(
        message.chat.id,
        text = 'Привет! Я бот, который поможет тебе найти быструю работу или разместить своё объявление с предложением.\n'
        'Но для начала тебе необходимо ознакомиться с некоторыми правилами и юридическими аспектами, чтобы не стать жертвой мошенников.\n'
        'Для этого перейди по <b><a href = "https://telegra.ph/Pravila-polzovaniya-telegram-botom-02-25">ссылке</a></b> и прочти обязательно правила!\n'
        'Ваша дальнейшая регистрация автоматически подтверждает, что Вы ознакомились с правилами.',
        parse_mode = 'HTML',
        reply_markup = markup
    )

    


