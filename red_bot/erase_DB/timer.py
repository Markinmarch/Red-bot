from threading import Timer


from red_bot.erase_DB.erase_DB import EraseDataBases
from red_bot.settings.config import DROP_TIME


def timer_to_erase():
    timer = Timer(
        interval = DROP_TIME,
        function = EraseDataBases.erase_databases()
    )
    timer.start()