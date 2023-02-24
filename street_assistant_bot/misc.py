import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from street_assistant_bot import config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')

storage = RedisStorage2(host=config.REDIS_HOST, port=config.REDIS_PORT, db=5)
dp = Dispatcher(bot, storage=storage)

async def on_shutdown(dp):
    await storage.close()
    await bot.close()

def main():
    from street_assistant_bot import handlers

    executor.start_polling(
        dp,
        skip_updates=True,
        on_shutdown=on_shutdown
    )