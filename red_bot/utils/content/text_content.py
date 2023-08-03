"""
Текстовые сообщения вынесены в отдельный файл
для быстрого и более эффективного форматирования
"""


WELCOME = (
    'Я бот, который поможет Вам найти быструю работу или разместить своё объявление с предложением.\n'
    'Но для начала Вам необходимо ознакомиться с некоторыми правилами и юридическими аспектами, чтобы не стать жертвой мошенников.\n'
    'Для этого перейди по <b><a href = "https://telegra.ph/Pravila-polzovaniya-telegram-botom-02-25">ссылке</a></b> и прочти обязательно правила!\n'
    'Ваша дальнейшая регистрация автоматически подтверждает, что Вы ознакомились с правилами.'
)

UNREGISTRED_USER = '{0}, Вы не зарегистрированный пользователь. Пожалуйста, пройдите регистрацию'

IF_USER_HAVE_ACCOUNT = '<b>У Вас имеется учётная запись</b>'

POST_INSTRUCTION = (
    'Напоминаем, что в пользовательских правилах во втором разделе есть инструкция с примерами по наполнению содержанием записи на канале.\n'
    'Если Вы забыли или не ознакамливались с инструкцией, то рекомендуем с ней ознакомиться. Там много полезной информации с примерами.\n'
    'Для ознакомления с инструкцией перейдите по <b><a href = "https://telegra.ph/Pravila-polzovaniya-telegram-botom-02-25">ссылке</a></b>'
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

REGISTRATION_FILTER = {
    'name_filter': 'Пожалуйста, повторите попытку. В псевдониме не должно быть никаких цифр и других символов - только буквы.',
    'age_filter': 'Пожалуйста, укажите возраст только цифрами.',
    'gender_filter': 'Пожалуйста, выберите один из двух вариантов.'
}

REGISTRATION_MESSAGE = {
    'add_name': 'Пожалуйста, введите своё имя. Можно использовать псевдоним для дополнителной безопасности.',
    'add_age': 'Укажите свой действительный возраст.',
    'add_gender': 'Укажите свой пол.',
    'add_phone': 'Согласны дать нам свой номер телефона?'
}

CREATE_POST_MESSAGE = {
    'direction': 'Пожалуйста, определите тему для Вашей записи',
    'title': 'Напишите краткое описание записи (напр. Подработка/Услуги сантехника/Дрова/Уголь/Вывезти мусор)',
    'text': 'Напишите содержание записи с подробностями',
    'conditions': 'Опишите условия работы - зарплату/цену за заказ',
    'photo': 'Можете прикрепить одну фотографию к записи по желанию либо опубликовать свою запись сразу'
}

PUBLICATION_ACCOUNCEMENT = 'Ваше объявление в ближайшее время будет опубликовано на канале'

UPDATE_MESSAGE = 'Обновите чат-бот, чтобы обновилось меню. Для этого закройте телеграм и зайдите вновь'

OUTSIDER_MESSAGE = 'К сожалению, мы не можем предоставить Вам право пользоваться телеграм-каналом'

BEFORE_DEL_ACC_MESSAGE = 'Если Вы удалите свой аккаунт, то и все Ваши записи с канала будут удалены. У Вас больше не будет возможности создавать посты, но Вы по прежнему сможете отзываться на них.'

DELETE_ACCOUNT_MESSAGE = 'Ваш аккаунт удалён'

WAITING_MESSAGE = 'Вы слишком часто используете эту команду. Подождите 5 минут'

WARNING_MESSAGE_BEFORE_DELETION_ACC = (
    'Если Вы удалите свой аккаунт, то и все Ваши записи с канала будут удалены.\n'
    'У Вас больше не будет возможности создавать посты, но Вы по прежнему сможете отзываться на них.'
)

ALREADY_RESPONDED_MESSAGE = 'Вы уже отзывались на этот пост. Если пост ещё актуален, то автор Вам напишет'

LIMIT_WARNING_PUBLICATION_MESSAGE = 'Ваш лимит подаваемых объявлений на сегодня закончился.'

INTERRUPTION_MESSAGE = 'Процесс прерван из-за долгого ожидания ответа.'