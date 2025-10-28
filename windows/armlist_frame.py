from PySide6.QtWidgets import QFrame
from PySide6.QtCore import QSize, QByteArray
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QFontDatabase, QFont
from windows.ui.ui_armlistFrame import Ui_ArmlistFrame
import ast


class ArmlistFrame(QFrame, Ui_ArmlistFrame):
    def __init__(self, armlist_id: int, name: str, cost: int, rank: int, fraction_id: int, image: bytearray, fraction_color: str):
        super().__init__()
        self.armlist_id = armlist_id
        self.name = name
        self.cost = cost
        self.rank = rank
        self.fraction_id = fraction_id
        self.image = image
        self.fraction_color = fraction_color
        self.darkgrey_color = '#6F7378'
        self.font_id = QFontDatabase.addApplicationFont(":/fonts/BravoRG.otf")
        self.setupUi(self)
        self.setFixedSize(QSize(210, 260))
        # self.setMinimumSize(QSize(200, 250))
        
        self.set_labels()
        self.set_fraction_color()
        self.set_image()
    
    # Установка значений лейблам
    def set_labels(self):
        font_families = QFontDatabase.applicationFontFamilies(self.font_id)
        font_name = font_families[0]
        custom_font = QFont(font_name, 16)
        custom_font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 1)
        self.NameLabel.setFont(custom_font)
        self.CostLabel.setFont(custom_font)
        self.RankLabel.setFont(custom_font)

        self.NameLabel.setText(self.name)
        self.RankLabel.setText(f'Ранг {self.rank}')
        self.CostLabel.setText(f'Стоим. {self.cost}')
    
    # Установка изображения
    def set_image(self):
        if self.image:
            image_data = ast.literal_eval(self.image)
            byte_array = QByteArray(image_data)
            pixmap = QPixmap()
            pixmap.loadFromData(byte_array)
            self.ImageLabel.setPixmap(pixmap)
        else:
            self.ImageLabel.setText("Изображение не найдено")

    # Установка цвета в зависимости от фракции
    def set_fraction_color(self):
        self.NameLabel.setStyleSheet(f'background-color: {self.fraction_color}; color: white;')
        self.ParametersFrame.setStyleSheet(f'QFrame{{background-color: {self.darkgrey_color}; border: none;}} QLabel{{border: 1px solid {self.fraction_color}; color: white;}}')
