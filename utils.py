import os
import json
import glob
import logging
from datetime import datetime
from typing import Literal


# Чтение json
def read_json(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Чистка директории при переполнении
def clean_folder(folder: str, file_format: str, max_file_count: int):
    files = glob.glob(folder + file_format)
    if len(files) > max_file_count:
        oldest_file = min(files, key=os.path.getctime)
        os.remove(oldest_file)

# Запись информации в терминал и в логи
def log(text: str, type: Literal['info', 'warning', 'error'] = 'info'):
    print(text)
    match type:
        case 'info':
            logging.info(text)
        case 'warning':
            logging.warning(text)
        case 'error':
            logging.error(text)

# Получение текущей даты
def get_today_date():
    return datetime.now().strftime("%d.%m.%Y_%H-%M-%S")
