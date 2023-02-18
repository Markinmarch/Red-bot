from street_assistant_bot import config
from street_assistant_bot.misc import main, logger


if not config.BOT_TOKEN or not config.DB_NAME:
    raise ValueError(
        "TELEGRAM_BOT_TOKEN and DB_NAME env variables "
        "wasn't implemented in .env (both should be initialized)."
    )


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())

