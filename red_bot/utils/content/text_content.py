"""
Текстовые сообщения вынесены в отдельный файл
для быстрого и более эффективного форматирования
"""

from ...settings.config import RULES_URL

WELCOME = (
    'Я бот, который поможет Вам найти быструю работу или разместить своё объявление с предложением.\n'
    'Но для начала Вам необходимо ознакомиться с некоторыми правилами и юридическими аспектами, чтобы не стать жертвой мошенников.\n'
    f'Для этого перейди по <b><a href = {RULES_URL}>ссылке</a></b> и прочтите обязательно правила!\n'
    '<b>Ваша дальнейшая регистрация автоматически подтверждает, что Вы ознакомились с правилами.</b>'
)

UNREGISTRED_USER = '{0}, Вы не зарегистрированный пользователь. Пожалуйста, пройдите регистрацию'

IF_USER_HAVE_ACCOUNT = '<b>У Вас имеется учётная запись</b>'

POST_INSTRUCTION = (
    'Напоминаем о пользовательских правилах.\n'
    'Если Вы забыли или не ознакамливались с инструкцией, то рекомендуем с ней ознакомиться.\n'
    f'Для ознакомления с инструкцией перейдите по <b><a href = {RULES_URL}>ссылке</a></b>'
)

POST_CONTENT = (
    '<b><u>{0}</u></b>\n'
    '<b>→ Содержание:</b> {1}\n'
    '<b>→ Условия:</b> <i>{2}</i>'
)

BAD_WORDS = [
    'блядь',
    'сука',
    'жопа',
    'пизда',
    'хуй',
    'нахуй',
    'пидорас'
]

FEEDBACK = 'Пользователь <a href="{0}">{1}</a> отозвался на Ваше <a href="{2}/{3}">объявление</a>.'

BEFORE_TO_SEND_MESSAGE_ADMINS = 'Напишите (без мата), что Вы хотите сообщить администрации канала?'

MESSAGE_TO_ADMIN = 'Пользователь <a href="{0}">{1}</a> обратился с предложением:\n'

URL_FZ_5 = 'https://www.consultant.ru/document/cons_doc_LAW_110165/cdde38fe25c37368ccc014de994e36cf128d5318/'

URL_FZ_152 = 'https://www.consultant.ru/document/cons_doc_LAW_61801/'

REGISTRATION_MESSAGE = (
    f'Согласно <a href="{URL_FZ_152}"><b>Федерального закона № 152-ФЗ <u>"О персональных данных"</u></b></a> при нажатии на кнопку "Согласен" Вы соглашаетесь передать Ваши персональные'
    'данные в виде номера телефона без последующей передачи третьим лицам, за исключением случаев предусмотренным Законом Российской Федерации, например:'
    f'<a href="{URL_FZ_5}"><b>ст.ст. № 4, 5 Федерального закона № 3-ФЗ <u>"О полиции"</u></b></a>'
)

CREATE_POST_MESSAGE = {
    'title': 'Выберите один из предложенных вариантов',
    'text': 'Напишите содержание записи с подробностями',
    'conditions': 'Опишите условия работы - зарплату/цену за заказ <i>(только цифрами либо по кнопке)</i>',
    'photo': 'Можете прикрепить одну фотографию к записи по желанию либо опубликовать свою запись сразу'
}

PUBLICATION_ACCOUNCEMENT = 'Ваше объявление опубликовано на канале'

UPDATE_MESSAGE = 'Поздравляем, вы успешно прошли регистрацию'

OUTSIDER_MESSAGE = 'К сожалению, мы не можем предоставить Вам право пользоваться телеграм-каналом'

BEFORE_DEL_ACC_MESSAGE = 'Если Вы удалите свой аккаунт, то и все Ваши записи с канала будут удалены. У Вас больше не будет возможности создавать посты, но Вы по прежнему сможете отзываться на них.'

DELETE_ACCOUNT_MESSAGE = 'Ваш аккаунт удалён'

WARNING_MESSAGE_BEFORE_DELETION_ACC = (
    'Если Вы удалите свой аккаунт, то и все Ваши записи с канала будут удалены.\n'
    'У Вас больше не будет возможности создавать посты, но Вы по прежнему сможете отзываться на них.'
)

FEEDBACK_SEND = 'Отзыв отправлен'

ALREADY_RESPONDED_MESSAGE = 'Вы уже отзывались на эту запись. Если запись ещё актуальна, то её автор Вам напишет'

LIMIT_WARNING_PUBLICATION_MESSAGE = 'Ваш лимит подаваемых записей на сегодня закончился.'

INTERRUPTION_MESSAGE = 'Процесс прерван из-за долгого ожидания ответа.'

CHECK_POSTS = 'Выберите номер записи из предложенного списка:'

NONE_POSTS = 'У Вас не имеется записей на канале.'

DELETE_POST_MESSAGE = 'Ваша запись удалёна.'

FILTERS_MESSAGE = {
    'command_brake': 'Команда отменена.',
    'none_this_post': 'У Вас не имеется записи под данным номером.',
    'bad_words': 'Пожалуйста, не используйте ненормативную лексику.\n'
                 'Помните о <b><a href = "https://telegra.ph/Pravila-polzovaniya-telegram-botom-02-25">правилах</a></b> пользования каналом!',
    'create_post': {
        'repeat_title': 'Пожалуйста, выберите из предложенных вариатнов.',
        'repeat_text': 'Пожалуйста, опишите деятельность подробнее. Необходимо написать не менее двадцати символов.',
        'repeat_condition': 'Пожалуйста, укажите цену либо нажмите на кнопку "По договорённости"',
    },
    'registration_user': {
        'add_name': 'Пожалуйста, введите своё имя. Можно использовать псевдоним для дополнителной безопасности.',
        'add_age': 'Укажите свой действительный возраст.',
        'add_gender': 'Укажите свой пол.',
        'add_phone': 'Согласны дать нам свой номер телефона?'
    },
}
