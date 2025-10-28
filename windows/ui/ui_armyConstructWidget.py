# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'armyConstructWidgetNLKCZj.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QScrollArea, QSizePolicy,
    QToolButton, QVBoxLayout, QWidget)
import res_rc

class Ui_armyConstructWidget(object):
    def setupUi(self, armyConstructWidget):
        if not armyConstructWidget.objectName():
            armyConstructWidget.setObjectName(u"armyConstructWidget")
        armyConstructWidget.resize(802, 634)
        armyConstructWidget.setStyleSheet(u"#armyConstructWidget{background-color: lightgrey;}\n"
"#FiltersFrame, #AllArmlistMainFrame, #UserArmlistMainFrame{\n"
"border-radius: 5px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(armyConstructWidget)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.FiltersFrame = QFrame(armyConstructWidget)
        self.FiltersFrame.setObjectName(u"FiltersFrame")
        self.FiltersFrame.setMinimumSize(QSize(0, 40))
        self.FiltersFrame.setMaximumSize(QSize(16777215, 40))
        self.FiltersFrame.setStyleSheet(u"#FiltersFrame{background-color: white;}")
        self.FiltersFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.FiltersFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.FiltersFrame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.SortFrame = QFrame(self.FiltersFrame)
        self.SortFrame.setObjectName(u"SortFrame")
        self.SortFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.SortFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.SortFrame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SortLabel = QLabel(self.SortFrame)
        self.SortLabel.setObjectName(u"SortLabel")
        font = QFont()
        font.setPointSize(11)
        self.SortLabel.setFont(font)

        self.horizontalLayout.addWidget(self.SortLabel)

        self.SortComboBox = QComboBox(self.SortFrame)
        self.SortComboBox.setObjectName(u"SortComboBox")
        self.SortComboBox.setMinimumSize(QSize(250, 0))
        self.SortComboBox.setMaximumSize(QSize(250, 16777215))
        self.SortComboBox.setFont(font)
        self.SortComboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.SortComboBox)

        self.SortToolButton = QToolButton(self.SortFrame)
        self.SortToolButton.setObjectName(u"SortToolButton")
        self.SortToolButton.setMinimumSize(QSize(26, 26))
        self.SortToolButton.setMaximumSize(QSize(26, 26))
        self.SortToolButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SortToolButton.setStyleSheet(u"border: None;")
        icon = QIcon()
        icon.addFile(u":/images/sort_down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SortToolButton.setIcon(icon)
        self.SortToolButton.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.SortToolButton)


        self.horizontalLayout_2.addWidget(self.SortFrame, 0, Qt.AlignmentFlag.AlignLeft)

        self.HelpToolButton = QToolButton(self.FiltersFrame)
        self.HelpToolButton.setObjectName(u"HelpToolButton")
        self.HelpToolButton.setMinimumSize(QSize(26, 26))
        self.HelpToolButton.setMaximumSize(QSize(26, 26))
        self.HelpToolButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.HelpToolButton.setStyleSheet(u"border: None;")
        icon1 = QIcon()
        icon1.addFile(u":/images/faq.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HelpToolButton.setIcon(icon1)
        self.HelpToolButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_2.addWidget(self.HelpToolButton)


        self.verticalLayout_3.addWidget(self.FiltersFrame)

        self.AllArmlistMainFrame = QFrame(armyConstructWidget)
        self.AllArmlistMainFrame.setObjectName(u"AllArmlistMainFrame")
        self.AllArmlistMainFrame.setMinimumSize(QSize(0, 250))
        self.AllArmlistMainFrame.setMaximumSize(QSize(16777215, 500))
        self.AllArmlistMainFrame.setStyleSheet(u"#AllArmlistMainFrame{background-color: white;}")
        self.AllArmlistMainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.AllArmlistMainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.AllArmlistMainFrame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 5, 2)
        self.AllInfoLabelFrame = QFrame(self.AllArmlistMainFrame)
        self.AllInfoLabelFrame.setObjectName(u"AllInfoLabelFrame")
        self.AllInfoLabelFrame.setMinimumSize(QSize(0, 26))
        self.AllInfoLabelFrame.setMaximumSize(QSize(16777215, 26))
        self.AllInfoLabelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.AllInfoLabelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.AllInfoLabelFrame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 5, 0)
        self.AllArmlistLabel = QLabel(self.AllInfoLabelFrame)
        self.AllArmlistLabel.setObjectName(u"AllArmlistLabel")
        self.AllArmlistLabel.setFont(font)

        self.horizontalLayout_4.addWidget(self.AllArmlistLabel)


        self.verticalLayout.addWidget(self.AllInfoLabelFrame)

        self.AllScrollArea = QScrollArea(self.AllArmlistMainFrame)
        self.AllScrollArea.setObjectName(u"AllScrollArea")
        self.AllScrollArea.setMinimumSize(QSize(0, 250))
        self.AllScrollArea.setMaximumSize(QSize(16777215, 500))
        self.AllScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.AllScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.AllScrollArea.setWidgetResizable(True)
        self.AllScrollAreaWidgetContents = QWidget()
        self.AllScrollAreaWidgetContents.setObjectName(u"AllScrollAreaWidgetContents")
        self.AllScrollAreaWidgetContents.setGeometry(QRect(0, 0, 780, 252))
        self.AllGridLayout = QGridLayout(self.AllScrollAreaWidgetContents)
        self.AllGridLayout.setSpacing(12)
        self.AllGridLayout.setObjectName(u"AllGridLayout")
        self.AllGridLayout.setContentsMargins(8, 8, 8, 8)
        self.AllScrollArea.setWidget(self.AllScrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.AllScrollArea)


        self.verticalLayout_3.addWidget(self.AllArmlistMainFrame)

        self.UserArmlistMainFrame = QFrame(armyConstructWidget)
        self.UserArmlistMainFrame.setObjectName(u"UserArmlistMainFrame")
        self.UserArmlistMainFrame.setMinimumSize(QSize(0, 250))
        self.UserArmlistMainFrame.setMaximumSize(QSize(16777215, 500))
        self.UserArmlistMainFrame.setStyleSheet(u"#UserArmlistMainFrame{background-color: white;}")
        self.UserArmlistMainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.UserArmlistMainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.UserArmlistMainFrame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 2)
        self.UserInfoLabelFrame = QFrame(self.UserArmlistMainFrame)
        self.UserInfoLabelFrame.setObjectName(u"UserInfoLabelFrame")
        self.UserInfoLabelFrame.setMinimumSize(QSize(0, 26))
        self.UserInfoLabelFrame.setMaximumSize(QSize(16777215, 26))
        self.UserInfoLabelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.UserInfoLabelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.UserInfoLabelFrame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 5, 0)
        self.UserArmlistLabel = QLabel(self.UserInfoLabelFrame)
        self.UserArmlistLabel.setObjectName(u"UserArmlistLabel")
        self.UserArmlistLabel.setFont(font)

        self.horizontalLayout_5.addWidget(self.UserArmlistLabel)

        self.UserCostLabel = QLabel(self.UserInfoLabelFrame)
        self.UserCostLabel.setObjectName(u"UserCostLabel")
        self.UserCostLabel.setFont(font)

        self.horizontalLayout_5.addWidget(self.UserCostLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.UserInfoLabelFrame)

        self.UserScrollArea = QScrollArea(self.UserArmlistMainFrame)
        self.UserScrollArea.setObjectName(u"UserScrollArea")
        self.UserScrollArea.setMinimumSize(QSize(0, 250))
        self.UserScrollArea.setMaximumSize(QSize(16777215, 500))
        self.UserScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.UserScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 780, 252))
        self.UserGridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.UserGridLayout.setSpacing(12)
        self.UserGridLayout.setObjectName(u"UserGridLayout")
        self.UserGridLayout.setContentsMargins(8, 8, 8, 8)
        self.UserScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.UserScrollArea)


        self.verticalLayout_3.addWidget(self.UserArmlistMainFrame)


        self.retranslateUi(armyConstructWidget)

        QMetaObject.connectSlotsByName(armyConstructWidget)
    # setupUi

    def retranslateUi(self, armyConstructWidget):
        armyConstructWidget.setWindowTitle(QCoreApplication.translate("armyConstructWidget", u"armyConstructWidget", None))
        self.SortLabel.setText(QCoreApplication.translate("armyConstructWidget", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e", None))
        self.SortToolButton.setText("")
        self.HelpToolButton.setText("")
        self.AllArmlistLabel.setText(QCoreApplication.translate("armyConstructWidget", u"\u0412\u0441\u0435 \u043e\u0442\u0440\u044f\u0434\u044b", None))
        self.UserArmlistLabel.setText(QCoreApplication.translate("armyConstructWidget", u"\u041c\u043e\u0438 \u043e\u0442\u0440\u044f\u0434\u044b", None))
        self.UserCostLabel.setText(QCoreApplication.translate("armyConstructWidget", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0430\u0440\u043c\u0438\u0438", None))
    # retranslateUi

