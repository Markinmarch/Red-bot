import schedule


from auto_control_DB.check_DB.queue import get_queue
from red_bot.settings.config import DROP_TIME


if __name__ == '__main__':
    while True:
        schedule.every().day.at(DROP_TIME).do(get_queue)
        schedule.run_pending()