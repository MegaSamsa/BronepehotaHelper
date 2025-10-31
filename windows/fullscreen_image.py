from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QSize, QByteArray, Qt
from PySide6.QtGui import QPixmap, QFontDatabase, QFont, QMouseEvent
from windows.ui.ui_fullscreenImageDialog import Ui_FullscreenImageDialog
import ast


class FullscreenImage(QDialog, Ui_FullscreenImageDialog):
    def __init__(self, image: bytearray):
        super().__init__()
        self.image = image
        # self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)

        self.set_image()
    
    # Установка изображения
    def set_image(self):
        if self.image:
            image_data = ast.literal_eval(self.image)
            byte_array = QByteArray(image_data)
            pixmap = QPixmap()
            pixmap.loadFromData(byte_array)
            self.ImageLabel.setPixmap(pixmap)
            self.setFixedSize(pixmap.size())
        else:
            self.ImageLabel.setText("Изображение не найдено")

    # Обработка закрытия окна при нажатии Escape
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    # Обработка закрытия окна при нажатии клавиш мыши
    def mousePressEvent(self, event):
        self.close()