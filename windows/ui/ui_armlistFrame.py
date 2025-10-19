# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'armlistFrameXbwKLK.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ArmlistFrame(object):
    def setupUi(self, ArmlistFrame):
        if not ArmlistFrame.objectName():
            ArmlistFrame.setObjectName(u"ArmlistFrame")
        ArmlistFrame.resize(312, 317)
        ArmlistFrame.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        ArmlistFrame.setStyleSheet(u"#ArmlistFrame {\n"
"	background-color: lightgrey;\n"
"    border: 1.5px solid #6F7378;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#ArmlistFrame:hover {\n"
"	border: 2px solid #444444;\n"
"}")
        self.verticalLayout = QVBoxLayout(ArmlistFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.NameLabel = QLabel(ArmlistFrame)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setPointSize(11)
        self.NameLabel.setFont(font)
        self.NameLabel.setStyleSheet(u"#NameLabel{\n"
"	color: white;\n"
"	background-color: darkred;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}")
        self.NameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NameLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.NameLabel)

        self.CostLabel = QLabel(ArmlistFrame)
        self.CostLabel.setObjectName(u"CostLabel")
        self.CostLabel.setMaximumSize(QSize(16777215, 30))
        self.CostLabel.setFont(font)
        self.CostLabel.setStyleSheet(u"#CostLabel{\n"
"	background-color: #6F7378;\n"
"	color: white;\n"
"}")
        self.CostLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.CostLabel)

        self.ImageLabel = QLabel(ArmlistFrame)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setMinimumSize(QSize(50, 50))
        self.ImageLabel.setFont(font)
        self.ImageLabel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.ImageLabel)


        self.retranslateUi(ArmlistFrame)

        QMetaObject.connectSlotsByName(ArmlistFrame)
    # setupUi

    def retranslateUi(self, ArmlistFrame):
        ArmlistFrame.setWindowTitle(QCoreApplication.translate("ArmlistFrame", u"Frame", None))
        self.NameLabel.setText(QCoreApplication.translate("ArmlistFrame", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0442\u0440\u044f\u0434\u0430", None))
        self.CostLabel.setText(QCoreApplication.translate("ArmlistFrame", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u0442\u0440\u044f\u0434\u0430", None))
        self.ImageLabel.setText(QCoreApplication.translate("ArmlistFrame", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
    # retranslateUi

