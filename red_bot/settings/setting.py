import logging


from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.redis import RedisStorage2


from red_bot.settings import config


logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
logger = logging.getLogger(__name__)

bot = Bot(
    token = config.BOT_TOKEN,
    parse_mode = 'HTML'
)

storage = RedisStorage2(
    host = config.REDIS_HOST,
    port = config.REDIS_PORT,
    db = config.REDIS_BD
)
dp = Dispatcher(
    bot,
    storage = storage
)


def main():
    from red_bot import app, test

    executor.start_polling(
        dp,
        skip_updates = True
    )