import sqlite3
from typing import Literal


# Класс подключения к БД
class DBConnector():
    def __init__(self, db_file: str):
        self._connection = sqlite3.connect(db_file)
        self._cursor = self._connection.cursor()

    # Получение данных
    def get_data(self, request: str, count: Literal['all', 'one']):
        self._cursor.execute(request)

        if count == 'all':
            return self._cursor.fetchall()
        elif count == 'one':
            return self._cursor.fetchone()
    
    # Запись данных
    def set_data(self, request: str):
        self._cursor.execute(request)
        self._connection.commit()

    def execute(self, request):
        self._cursor.execute(request)

    def fetchall(self):
        return self._cursor.fetchall()
    
    def fetchone(self):
        return self._cursor.fetchone()
