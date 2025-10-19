from PySide6.QtWidgets import QMainWindow
from windows.ui.ui_mainWindow import Ui_MainWindow
from db_requests.db_connector import DBConnector
from db_requests.fractions_requests import *
from windows.army_construct_widget import ArmyConstructWidget
from utils import log


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, db_connector: DBConnector):
        super().__init__()
        self.setupUi(self)
        self.set_preferences()
        self.get_button_connections()
        self.db_connector = db_connector
        self.fractions_info = self.get_fractions_info()
        self.section = 'main'
    
        log("Инициализация завершена. Программа запущена")
        self.open_army_construct()
    
    # Применение настроек
    def set_preferences(self):
        self.showMaximized()

    # Подлючение сигналов
    def get_button_connections(self):
        self.ArmyConstructPushButton.clicked.connect(self.open_army_construct)
        self.ProgramInfoPushButton.clicked.connect(self.open_program_info)
        self.ErrorReportPushButton.clicked.connect(self.open_error_report)

    # Открытие конструктора отрядов
    def open_army_construct(self):
        if not self.section == 'army_construct':
            self.section = 'army_construct'
            self.RightMenuFrame.hide()
            army_construct = ArmyConstructWidget(self.db_connector, self.fractions_info)
            self.horizontalLayout.addWidget(army_construct)

    # Отображение информации о программе
    def open_program_info(self):
        pass

    # Отображение окна сообщения об ошибке
    def open_error_report(self):
        pass

    # Получение информации о фракциях
    def get_fractions_info(self):
        return get_all_fractions(self.db_connector)
