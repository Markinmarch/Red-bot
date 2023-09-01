from threading import Timer
import logging


from red_bot.erase_DB.write_DB import write_data_to_json
from red_bot.erase_DB.erase_DB import erase_databases
from red_bot.settings.config import DROP_TIME


def timer_to_erase():
    #таймер записи данных в JSON
    write_timer = Timer(
        interval = DROP_TIME,
        function = write_data_to_json()
    )
    #таймер сброса дынных из БД
    erase_timer = Timer(
        interval = DROP_TIME,
        function = erase_databases()
    )

    write_timer.start()
    erase_timer.start()

    logging.info('!!! TIMER START !!!')
