# Red bot
Телеграм-бот разработанный на базе библиотеки aiogram версии 3.1.1 <!-- описание репозитория -->

<!--Установка-->
## Установка (Linux)
У вас должны быть установлены [зависимости проекта](https://github.com/Markinmarch/Red-bot#зависимости)

1. Клонирование репозитория 

```git clone https://github.com/Markinmarch/Red-bot.git```

2. Переход в директорию Oxygen

```cd Red-bot```

3. Установка пакета нереляционной базы данных [Redis](https://redis.io/docs/install/install-redis/install-redis-on-linux/)

4. Создание виртуального окружения

```python3 -m venv .venv```

5. Активация виртуального окружения

```source .venv/bin/activate```

6. Запуск нереляционной базы данных Redis

```sudo service redis-server start```

7. Во время принудительной остановки приложения следует обязательно осуществлять очистку нереляционной БД

```redis-cli fulshall``` или ```redis-cli flushdb 0```

8. Установка зависимостей

```pip install -r requirements.txt```

9. Запуск скрипта для демонстрации возможностей Red bot в [фоновом](https://losst.pro/kak-zapustit-protsess-v-fone-linux) режиме 

```python -m red_bot & python -m control_DB &```

<!-- Пользовательская документация
## Документация
Пользовательскую документацию можно получить по [этой ссылке](./docs/ru/index.md). -->

<!-- [Релизы программы]: https://github.com/OkulusDev/Oxygen/releases -->

<!--Поддержка-->
## Поддержка
Если у вас возникли сложности или вопросы по использованию пакета, создайте 
[обсуждение](https://github.com/Markinmarch/Red-bot/issues/new/choose) в данном репозитории или напишите на электронную почту <iztvmrk@mail.ru>.

<!--зависимости-->
## Зависимости
Эта программа зависит от интепретатора Python версии 3.7 или выше, PIP 23.2.1 или выше

<!-- описание коммитов
## Описание коммитов
| Название | Описание                                                        |
|----------|-----------------------------------------------------------------|
| build	   | Сборка проекта или изменения внешних зависимостей               |
| sec      | Безопасность, уязвимости                                        |
| ci       | Настройка CI и работа со скриптами                              |
| docs	   | Обновление документации                                         |
| feat	   | Добавление нового функционала                                   |
| fix	   | Исправление ошибок                                              |
| perf	   | Изменения направленные на улучшение производительности          |
| refactor | Правки кода без исправления ошибок или добавления новых функций |
| revert   | Откат на предыдущие коммиты                                     |
| style	   | Правки по кодстайлу (табы, отступы, точки, запятые и т.д.)      |
| test	   | Добавление тестов                                               | -->