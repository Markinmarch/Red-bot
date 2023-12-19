import logging


logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    try:
        from sql_db import main
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())
