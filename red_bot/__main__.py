import asyncio


from red_bot.settings.setting import logger, main


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())