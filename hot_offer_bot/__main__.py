from hot_offer_bot.core import config, settings


if not config.BOT_TOKEN or not config.DB_NAME:
    raise ValueError(
        "TELEGRAM_BOT_TOKEN and DB_NAME env variables "
        "wasn't implemented in .env (both should be initialized)."
    )

if __name__ == '__main__':
    try:
        settings.main()
    except Exception:
        import traceback

        settings.logger.warning(traceback.format_exc())