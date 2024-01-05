# -*- coding: utf-8 -*-

# Form generated from reading UI file 'menu.ui'
# Created by: Qt User Interface Compiler version 6.6.1

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QLabel, QMenuBar, QPushButton, QSizePolicy, QStatusBar, QVBoxLayout, QWidget)


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(800, 600)
        self.centralwidget = QWidget(MainMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(230, 150, 321, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.button_processes = QPushButton(self.verticalLayoutWidget)
        self.button_processes.setObjectName(u"button_processes")
        sizePolicy.setHeightForWidth(self.button_processes.sizePolicy().hasHeightForWidth())
        self.button_processes.setSizePolicy(sizePolicy)
        self.button_processes.setFont(font)

        self.verticalLayout.addWidget(self.button_processes)

        self.button_paging = QPushButton(self.verticalLayoutWidget)
        self.button_paging.setObjectName(u"button_paging")
        sizePolicy.setHeightForWidth(self.button_paging.sizePolicy().hasHeightForWidth())
        self.button_paging.setSizePolicy(sizePolicy)
        self.button_paging.setFont(font)

        self.verticalLayout.addWidget(self.button_paging)

        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainMenu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 29))
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainMenu)
        self.statusbar.setObjectName(u"statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)

    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainMenu", u"Choose technology", None))
        self.button_processes.setText(QCoreApplication.translate("MainMenu", u"Processes scheduling", None))
        self.button_paging.setText(QCoreApplication.translate("MainMenu", u"Paging", None))
    # retranslateUi
