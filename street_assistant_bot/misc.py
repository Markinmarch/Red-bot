<<<<<<< HEAD
import logging
=======
import logging 
>>>>>>> parent of df8fba4 (подключение локальной БД)

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from street_assistant_bot import config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')

storage = RedisStorage2(host='localhost', port=6379, db=5)
dp = Dispatcher(bot, storage=storage)

<<<<<<< HEAD
async def on_shutdown(dp):
    await storage.close()
    await bot.close()
=======
>>>>>>> parent of df8fba4 (подключение локальной БД)

def main():
    from street_assistant_bot import handlers

    executor.start_polling(dp, skip_updates=True)