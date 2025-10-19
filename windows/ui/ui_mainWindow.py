# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindoweINhOm.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuFrame = QFrame(self.centralwidget)
        self.LeftMenuFrame.setObjectName(u"LeftMenuFrame")
        self.LeftMenuFrame.setMinimumSize(QSize(250, 0))
        self.LeftMenuFrame.setMaximumSize(QSize(250, 16777215))
        self.LeftMenuFrame.setStyleSheet(u"#LeftMenuFrame{background-color: grey;}\n"
"\n"
"QPushButton{\n"
"background-color: lightgrey;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"}")
        self.LeftMenuFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LeftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.LeftMenuFrame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.LogoLabel = QLabel(self.LeftMenuFrame)
        self.LogoLabel.setObjectName(u"LogoLabel")
        self.LogoLabel.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(11)
        self.LogoLabel.setFont(font)
        self.LogoLabel.setPixmap(QPixmap(u":/images/logo.png"))
        self.LogoLabel.setScaledContents(True)
        self.LogoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.LogoLabel)

        self.ButtonsFrame = QFrame(self.LeftMenuFrame)
        self.ButtonsFrame.setObjectName(u"ButtonsFrame")
        self.ButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ButtonsFrame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.ArmyConstructPushButton = QPushButton(self.ButtonsFrame)
        self.ArmyConstructPushButton.setObjectName(u"ArmyConstructPushButton")
        self.ArmyConstructPushButton.setMinimumSize(QSize(0, 30))
        self.ArmyConstructPushButton.setMaximumSize(QSize(16777215, 30))
        self.ArmyConstructPushButton.setFont(font)
        self.ArmyConstructPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.ArmyConstructPushButton)


        self.verticalLayout.addWidget(self.ButtonsFrame)

        self.LeftMenuVerticalSpacer = QSpacerItem(20, 307, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.LeftMenuVerticalSpacer)

        self.BottomButtonsFrame = QFrame(self.LeftMenuFrame)
        self.BottomButtonsFrame.setObjectName(u"BottomButtonsFrame")
        self.BottomButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.BottomButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.BottomButtonsFrame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.BottomLine = QFrame(self.BottomButtonsFrame)
        self.BottomLine.setObjectName(u"BottomLine")
        self.BottomLine.setFrameShape(QFrame.Shape.HLine)
        self.BottomLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.BottomLine)

        self.ProgramInfoPushButton = QPushButton(self.BottomButtonsFrame)
        self.ProgramInfoPushButton.setObjectName(u"ProgramInfoPushButton")
        self.ProgramInfoPushButton.setMinimumSize(QSize(0, 30))
        self.ProgramInfoPushButton.setMaximumSize(QSize(16777215, 30))
        self.ProgramInfoPushButton.setFont(font)
        self.ProgramInfoPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.ProgramInfoPushButton)

        self.ErrorReportPushButton = QPushButton(self.BottomButtonsFrame)
        self.ErrorReportPushButton.setObjectName(u"ErrorReportPushButton")
        self.ErrorReportPushButton.setMinimumSize(QSize(0, 30))
        self.ErrorReportPushButton.setMaximumSize(QSize(16777215, 30))
        self.ErrorReportPushButton.setFont(font)
        self.ErrorReportPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.ErrorReportPushButton)


        self.verticalLayout.addWidget(self.BottomButtonsFrame)


        self.horizontalLayout.addWidget(self.LeftMenuFrame)

        self.RightMenuFrame = QFrame(self.centralwidget)
        self.RightMenuFrame.setObjectName(u"RightMenuFrame")
        self.RightMenuFrame.setStyleSheet(u"#RightMenuFrame{background-color: lightgrey;}")
        self.RightMenuFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RightMenuFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.RightMenuFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0411\u0440\u043e\u043d\u0435\u043f\u0435\u0445\u043e\u0442\u0430 Helper", None))
        self.LogoLabel.setText("")
        self.ArmyConstructPushButton.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u043e\u0440 \u043e\u0442\u0440\u044f\u0434\u043e\u0432", None))
        self.ProgramInfoPushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.ErrorReportPushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0438\u0442\u044c \u043e\u0431 \u043e\u0448\u0438\u0431\u043a\u0435", None))
    # retranslateUi

