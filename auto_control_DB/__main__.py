import time

if __name__ == '__main__':
    from auto_control_DB import check_DB
    while True:
        from .check_DB import *
        if time.strftime('%H') == DROP_TIME:
            write_datas
            erase_db
            time.sleep(check_DB.DAY)
        else:
            time.sleep(check_DB.HOUR)