import time

if __name__ == '__main__':
    from auto_control_DB import check_DB
    from red_bot.settings.config import DROP_TIME, HOUR, DAY
    while True:
        if time.strftime('%H') == DROP_TIME:
            from . check_DB import *
            write_datas
            erase_db
            time.sleep(DAY)
        else:
            time.sleep(HOUR)