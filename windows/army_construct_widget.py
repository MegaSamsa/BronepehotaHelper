from PySide6.QtWidgets import QWidget, QGridLayout
from windows.ui.ui_armyConstructWidget import Ui_armyConstructWidget
from PySide6.QtCore import QSize, Qt
from db_requests.db_connector import DBConnector
from db_requests.armlists_requests import *
from windows.armlist_frame import ArmlistFrame
from operator import attrgetter


class ArmyConstructWidget(QWidget, Ui_armyConstructWidget):
    def __init__(self, db_connector: DBConnector, fractions_info: list):
        super().__init__()
        self.setupUi(self)
        self.summary_list = []
        self.db_connector = db_connector
        self.fractions_info = fractions_info
        self.grid_width = 1024
        self.grid_objects_spacing = 16
        self.user_army_cost = 0
        
        self.get_armlists_from_db()
        self.get_sort_list()

    # Заполнение параметров сортировки
    def get_sort_list(self):
        self.sort_list = ['Название', 'Армейский ранг', 'Стоимость']
        self.SortComboBox.addItems(self.sort_list)
        self.SortComboBox.setCurrentIndex(0)

    # Получение армлистов из БД
    def get_armlists_from_db(self):
        self.armlists = get_all_armlists(self.db_connector, 'cost', is_init=True)
        self.summary_list = self.armlists
        self.techlists = get_all_techlists(self.db_connector, 'cost', is_init=True)
        for var in range(len(self.techlists)):
            self.summary_list.append(self.techlists[var])
        self.summary_list.sort(key=attrgetter('cost'), reverse=True)
    
    # Создание карточек армлистов и заполнение сетки
    def get_armlists_frames(self):
        while self.AllGridLayout.count():
            child = self.AllGridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        row_index = 0
        col_index = 0
        row_content_width_sum = 0
        for item in range(len(self.summary_list)):
            frac_color = self.get_fraction_by_id(self.summary_list[item].fraction_id)[2]
            armlist_frame = ArmlistFrame(self.summary_list[item].id,
                                         self.summary_list[item].name,
                                         self.summary_list[item].cost,
                                         self.summary_list[item].rank,
                                         self.summary_list[item].fraction_id,
                                         self.summary_list[item].image,
                                         frac_color)

            row_content_width_sum += armlist_frame.width() + self.grid_objects_spacing
            if row_content_width_sum > self.grid_width:
                row_content_width_sum = 0
                row_index += 1
                col_index = 0
            row = row_index
            col = col_index
            col_index += 1

            self.AllGridLayout.addWidget(armlist_frame, row, col)

    # Получение фракции по id
    def get_fraction_by_id(self, fraction_id: int):
        return [fraction for fraction in self.fractions_info if fraction[0] == fraction_id][0]

    def resizeEvent(self, event):
        self.grid_width = self.AllScrollAreaWidgetContents.width()
        self.get_armlists_frames()
    #     if self.AllArmlistMainFrame.width() != 100:
    #         self.AllArmlistFrame.setMaximumSize(QSize(self.AllArmlistMainFrame.width() - 5, self.AllArmlistMainFrame.height() - 31))
