import logging 

from aiogram import Bot, Dispatcher, types, executor
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage

from street_assistant_bot import config #???

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')

# storage = MemoryStorage()
storage = RedisStorage(host='localhost', port=6379, db=5)
dp = Dispatcher(bot, storage=storage)
dp.storage.close()


def main():
    from street_assistant_bot import handlers

    executor.start_polling(dp, skip_updates=True)
    
