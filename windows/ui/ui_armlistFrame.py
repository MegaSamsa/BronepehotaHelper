# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'armlistFrameqVNPxX.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ArmlistFrame(object):
    def setupUi(self, ArmlistFrame):
        if not ArmlistFrame.objectName():
            ArmlistFrame.setObjectName(u"ArmlistFrame")
        ArmlistFrame.resize(312, 317)
        ArmlistFrame.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        ArmlistFrame.setStyleSheet(u"#ArmlistFrame {\n"
"	background-color: lightgrey;\n"
"    border: 1.5px solid darkgrey;\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(ArmlistFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.NameLabel = QLabel(ArmlistFrame)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setMinimumSize(QSize(0, 45))
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

        self.ParametersFrame = QFrame(ArmlistFrame)
        self.ParametersFrame.setObjectName(u"ParametersFrame")
        self.ParametersFrame.setMinimumSize(QSize(0, 30))
        self.ParametersFrame.setMaximumSize(QSize(16777215, 30))
        self.ParametersFrame.setStyleSheet(u"QFrame{\n"
"background-color:  #6F7378;\n"
"border: none;\n"
"}\n"
"QLabel{\n"
"	color: white;\n"
"	border: 1px solid darkred;\n"
"}")
        self.ParametersFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ParametersFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.ParametersFrame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.RankLabel = QLabel(self.ParametersFrame)
        self.RankLabel.setObjectName(u"RankLabel")
        self.RankLabel.setMaximumSize(QSize(16777215, 16777215))
        self.RankLabel.setFont(font)
        self.RankLabel.setStyleSheet(u"")
        self.RankLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.RankLabel, 0, 0, 1, 2)

        self.CostLabel = QLabel(self.ParametersFrame)
        self.CostLabel.setObjectName(u"CostLabel")
        self.CostLabel.setMinimumSize(QSize(0, 0))
        self.CostLabel.setMaximumSize(QSize(16777215, 16777215))
        self.CostLabel.setFont(font)
        self.CostLabel.setStyleSheet(u"")
        self.CostLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.CostLabel, 0, 2, 1, 3)


        self.verticalLayout.addWidget(self.ParametersFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.ImageLabel = QLabel(ArmlistFrame)
        self.ImageLabel.setObjectName(u"ImageLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageLabel.sizePolicy().hasHeightForWidth())
        self.ImageLabel.setSizePolicy(sizePolicy)
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
        self.RankLabel.setText(QCoreApplication.translate("ArmlistFrame", u"\u0410\u0420", None))
        self.CostLabel.setText(QCoreApplication.translate("ArmlistFrame", u"\u0421\u0442\u043e\u0438\u043c.", None))
        self.ImageLabel.setText(QCoreApplication.translate("ArmlistFrame", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
    # retranslateUi

