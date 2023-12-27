# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogResult.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_DialogResult(object):
    def setupUi(self, DialogResult):
        if not DialogResult.objectName():
            DialogResult.setObjectName(u"DialogResult")
        DialogResult.resize(400, 300)
        self.horizontalLayoutWidget = QWidget(DialogResult)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 381, 231))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.table = QTableWidget(self.horizontalLayoutWidget)
        self.table.setObjectName(u"table")

        self.horizontalLayout.addWidget(self.table)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_result = QLabel(self.horizontalLayoutWidget)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setFont(font)
        self.label_result.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_result)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayoutWidget_2 = QWidget(DialogResult)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(210, 260, 181, 37))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_close = QPushButton(self.horizontalLayoutWidget_2)
        self.button_close.setObjectName(u"button_close")

        self.horizontalLayout_2.addWidget(self.button_close)


        self.retranslateUi(DialogResult)

        QMetaObject.connectSlotsByName(DialogResult)
    # setupUi

    def retranslateUi(self, DialogResult):
        DialogResult.setWindowTitle(QCoreApplication.translate("DialogResult", u"Results", None))
        self.label.setText(QCoreApplication.translate("DialogResult", u"The result is:", None))
        self.label_result.setText("")
        self.button_close.setText(QCoreApplication.translate("DialogResult", u"Close", None))
    # retranslateUi

