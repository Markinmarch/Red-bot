import time

if __name__ == '__main__':
    from control_DB import check_DB
    while True:
        from .check_DB import *
        if time.strftime('%H') == DROP_TIME:
            write_datas
            erase_db
            time.sleep(DAY)
        else:
            time.sleep(HOUR)