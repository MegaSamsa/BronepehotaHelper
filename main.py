import logging
from PySide6.QtWidgets import QApplication
from db_requests.db_connector import DBConnector
from utils import read_json, clean_folder, get_today_date

from windows.main_window import MainWindow


# Константы
DATA_PATH = 'data/'
DB_FILENAME = 'database.db'
CONFIG_FILENAME = 'config.json'
LOGS_DIR = 'logs/'
LOGS_COUNT = 8

# Подключение к БД
DB_CONNECTOR = DBConnector(db_file=DATA_PATH + DB_FILENAME)

# Чтение конфига
config = read_json(DATA_PATH + CONFIG_FILENAME)

# Запись лога
clean_folder(folder=LOGS_DIR, file_format='*.log', max_file_count=LOGS_COUNT - 1)
logging.basicConfig(level=logging.INFO, filename=f'{LOGS_DIR}log_{get_today_date()}.log', filemode='w', encoding='utf-8', format='%(asctime)s %(levelname)s %(message)s')

# Старт программы
APP = QApplication()
main_window = MainWindow(DB_CONNECTOR)
main_window.show()
APP.exec()
