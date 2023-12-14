import logging
from redis import Redis


from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer


from red_bot.settings.config import BOT_TOKEN, REDIS_HOST, REDIS_PORT, REDIS_BD


logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
logger = logging.getLogger(__name__)

session = AiohttpSession(api = TelegramAPIServer.from_base('http://localhost:8082'))

bot = Bot(
    token = BOT_TOKEN,
    parse_mode = 'HTML',
    session = session
)

storage = RedisStorage(
    redis = Redis(
        host = REDIS_HOST,
        port = REDIS_PORT,
        db = REDIS_BD
    )
)

dp = Dispatcher()

async def main() -> None:
    from red_bot import app
    await dp.start_polling(bot)
