import sqlite3, logging
from redis import StrictRedis
import traceback

from telebot.async_telebot import AsyncTeleBot
from . import config

logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

logger = logging.getLogger(__name__)

bot = AsyncTeleBot(
    token = config.BOT_TOKEN,
    parse_mode = 'HTML',
    colorful_logs = True
)

cache = StrictRedis(
    host = config.REDIS_HOST,
    port = config.REDIS_PORT,
    db = 0
)

def main():
    logger.info(traceback.print_exc())
    from hot_offer_bot.app import handlers
    from hot_offer_bot.DB import db_map


    import asyncio

    asyncio.run(bot.polling())