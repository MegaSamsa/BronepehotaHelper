# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fullscreenImageDialogNyTlfW.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_FullscreenImageDialog(object):
    def setupUi(self, FullscreenImageDialog):
        if not FullscreenImageDialog.objectName():
            FullscreenImageDialog.setObjectName(u"FullscreenImageDialog")
        FullscreenImageDialog.setWindowModality(Qt.WindowModality.WindowModal)
        FullscreenImageDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(FullscreenImageDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ImageLabel = QLabel(FullscreenImageDialog)
        self.ImageLabel.setObjectName(u"ImageLabel")
        font = QFont()
        font.setPointSize(11)
        self.ImageLabel.setFont(font)
        self.ImageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.ImageLabel)


        self.retranslateUi(FullscreenImageDialog)

        QMetaObject.connectSlotsByName(FullscreenImageDialog)
    # setupUi

    def retranslateUi(self, FullscreenImageDialog):
        FullscreenImageDialog.setWindowTitle(QCoreApplication.translate("FullscreenImageDialog", u"\u041f\u043e\u043b\u043d\u043e\u0440\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.ImageLabel.setText(QCoreApplication.translate("FullscreenImageDialog", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
    # retranslateUi

