import logging
from aiogram import types


from auto_control_DB.check_DB.write_to_JSON import write_data_to_json
from auto_control_DB.check_DB.erase_SQL_Redis import erase_databases


def get_queue():
    logging.info('--- Start write and erase DBs ---')
    write_data_to_json()
    erase_databases()
