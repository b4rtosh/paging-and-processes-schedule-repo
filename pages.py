# -*- coding: utf-8 -*-

# Form generated from reading UI file 'pages.ui'
# Created by: Qt User Interface Compiler version 6.6.1


from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QCheckBox, QComboBox, QFormLayout, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QSpinBox, QWidget, QDialog, QTableWidgetItem, QHeaderView, QAbstractItemView)
from dialogResult import Ui_DialogResult
import page_gen

sequence = []


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(800, 600)
        self.centralwidget = QWidget(MainPages)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 20, 731, 461))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 13)
        self.label_data = QLabel(self.formLayoutWidget)
        self.label_data.setObjectName(u"label_data")
        font = QFont()
        font.setPointSize(11)
        self.label_data.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_data)

        self.check_data = QCheckBox(self.formLayoutWidget)
        self.check_data.setObjectName(u"check_data")
        self.check_data.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_data.sizePolicy().hasHeightForWidth())
        self.check_data.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        self.check_data.setFont(font1)
        self.check_data.setCheckable(True)
        self.check_data.setChecked(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.check_data)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(1, QFormLayout.LabelRole, self.verticalSpacer_6)

        self.label_size = QLabel(self.formLayoutWidget)
        self.label_size.setObjectName(u"label_size")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_size.sizePolicy().hasHeightForWidth())
        self.label_size.setSizePolicy(sizePolicy1)
        self.label_size.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_size)

        self.spin_size = QSpinBox(self.formLayoutWidget)
        self.spin_size.setObjectName(u"spin_size")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spin_size.sizePolicy().hasHeightForWidth())
        self.spin_size.setSizePolicy(sizePolicy2)
        self.spin_size.setMinimum(1)
        self.spin_size.setMaximum(98)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spin_size)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.verticalSpacer)

        self.label_amount = QLabel(self.formLayoutWidget)
        self.label_amount.setObjectName(u"label_amount")
        self.label_amount.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_amount)

        self.spin_amount = QSpinBox(self.formLayoutWidget)
        self.spin_amount.setObjectName(u"spin_amount")
        sizePolicy.setHeightForWidth(self.spin_amount.sizePolicy().hasHeightForWidth())
        self.spin_amount.setSizePolicy(sizePolicy)
        self.spin_amount.setMinimum(1)
        self.spin_amount.setMaximum(50)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.spin_amount)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.label_page = QLabel(self.formLayoutWidget)
        self.label_page.setObjectName(u"label_page")
        self.label_page.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_page)

        self.spin_page = QSpinBox(self.formLayoutWidget)
        self.spin_page.setObjectName(u"spin_page")
        sizePolicy.setHeightForWidth(self.spin_page.sizePolicy().hasHeightForWidth())
        self.spin_page.setSizePolicy(sizePolicy)
        self.spin_page.setMinimum(1)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.spin_page)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(7, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.label_algorithm = QLabel(self.formLayoutWidget)
        self.label_algorithm.setObjectName(u"label_algorithm")
        self.label_algorithm.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_algorithm)

        self.combo_algorithm = QComboBox(self.formLayoutWidget)
        self.combo_algorithm.setObjectName(u"combo_algorithm")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.combo_algorithm.sizePolicy().hasHeightForWidth())
        self.combo_algorithm.setSizePolicy(sizePolicy3)
        self.combo_algorithm.setFont(font1)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.combo_algorithm)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(110, 500, 581, 37))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_generate = QPushButton(self.horizontalLayoutWidget)
        self.button_generate.setObjectName(u"button_generate")
        self.button_generate.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.button_generate.sizePolicy().hasHeightForWidth())
        self.button_generate.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.button_generate)

        self.button_exit = QPushButton(self.horizontalLayoutWidget)
        self.button_exit.setObjectName(u"button_exit")
        sizePolicy4.setHeightForWidth(self.button_exit.sizePolicy().hasHeightForWidth())
        self.button_exit.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.button_exit)

        self.spin_page.valueChanged.connect(self.forbid_replay)
        self.spin_amount.valueChanged.connect(self.forbid_replay)
        self.check_data.stateChanged.connect(self.enable_options)

        self.button_generate.clicked.connect(self.generate)  # connect generate button to generate function
        self.combo_algorithm.addItem('FIFO')
        self.combo_algorithm.addItem('LRU')
        MainPages.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainPages)

        QMetaObject.connectSlotsByName(MainPages)

    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Generator", None))
        self.label_data.setText(QCoreApplication.translate("MainPages", u"Use data from previous test: ", None))
        self.check_data.setText(QCoreApplication.translate("MainPages", u"checked - yes", None))
        self.label_size.setText(QCoreApplication.translate("MainPages", u"Memory size:", None))
        self.label_amount.setText(QCoreApplication.translate("MainPages", u"Amount of pages in sequence:", None))
        self.label_page.setText(QCoreApplication.translate("MainPages", u"Maximum page number:", None))
        self.label_algorithm.setText(QCoreApplication.translate("MainPages", u"Choose algorithm:", None))
        self.button_generate.setText(QCoreApplication.translate("MainPages", u"Generate", None))
        self.button_exit.setText(QCoreApplication.translate("MainPages", u"Exit", None))

    # retranslateUi

    def generate(self):  # function to generate pages
        self.check_data.setEnabled(True)
        global sequence
        amount = self.spin_amount.value()
        max_page = self.spin_page.value()
        memory_size = self.spin_size.value()
        algorithm = self.combo_algorithm.currentText()
        if self.check_data.isChecked():  # if checked use data from previous test
            pages = sequence.copy()
        else:  # if not generate new pages
            pages = page_gen.generate_pages(amount, max_page)
            sequence = pages.copy()
        pages = page_gen.execute_algorithm(memory_size, pages, algorithm)
        page_gen.save_test(memory_size, amount, algorithm, max_page, pages, sequence)
        self.show_result(pages)
        self.check_data.setChecked(False)

    def forbid_replay(self):  # function to forbid replaying test
        self.check_data.setChecked(False)
        self.check_data.setEnabled(False)

    def enable_options(self):  # function to enable options
        if self.check_data.isChecked():
            self.spin_page.setEnabled(False)
            self.spin_amount.setEnabled(False)
        else:
            self.spin_page.setEnabled(True)
            self.spin_amount.setEnabled(True)

    def show_result(self, result):  # function to show result
        self.dialog = QDialog()
        self.dialog.ui = Ui_DialogResult()
        self.dialog.ui.setupUi(self.dialog)
        length = int((len(result) - 1) / 2)
        self.dialog.ui.table.setColumnCount(2)
        # resize each column
        self.dialog.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # disable editing
        self.dialog.ui.table.verticalHeader().setVisible(False)
        self.dialog.ui.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dialog.ui.table.setRowCount(length)
        self.dialog.ui.table.setHorizontalHeaderLabels(["Page", "Frame"])
        for i in range(length):  # add pages and frames to table
            self.dialog.ui.table.setItem(i, 0, QTableWidgetItem(str(result[i * 2])))
            self.dialog.ui.table.setItem(i, 1, QTableWidgetItem(str(result[i * 2 + 1])))
        self.dialog.ui.label_result.setText(str(result[-1]))
        self.dialog.ui.button_close.clicked.connect(self.dialog.close)
        self.dialog.exec()
