# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pages.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(800, 600)
        self.centralwidget = QWidget(MainPages)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_close = QPushButton(self.centralwidget)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(280, 450, 102, 35))
        MainPages.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainPages)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 29))
        self.menuPages_generator = QMenu(self.menubar)
        self.menuPages_generator.setObjectName(u"menuPages_generator")
        MainPages.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainPages)
        self.statusbar.setObjectName(u"statusbar")
        MainPages.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPages_generator.menuAction())

        self.retranslateUi(MainPages)

        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"MainWindow", None))
        self.button_close.setText(QCoreApplication.translate("MainPages", u"Close", None))
        self.menuPages_generator.setTitle(QCoreApplication.translate("MainPages", u"Pages generator", None))
    # retranslateUi

