# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'processes.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QLocale,
                            QMetaObject, QRect, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QCheckBox, QComboBox, QFormLayout,
                               QHBoxLayout, QLabel, QMenuBar,
                               QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
                               QStatusBar, QWidget)
import process_gen
from dialogResult import Ui_DialogResult
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QAbstractItemView

processes_list = []


class Ui_MainProcesses(object):
    def setupUi(self, MainProcesses):
        if not MainProcesses.objectName():
            MainProcesses.setObjectName(u"MainProcesses")
        MainProcesses.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainProcesses.sizePolicy().hasHeightForWidth())
        MainProcesses.setSizePolicy(sizePolicy)
        MainProcesses.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainProcesses)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 10, 731, 461))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 13)
        self.label_number = QLabel(self.formLayoutWidget)
        self.label_number.setObjectName(u"label_number")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_number.sizePolicy().hasHeightForWidth())
        self.label_number.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        self.label_number.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_number)

        self.spin_number = QSpinBox(self.formLayoutWidget)
        self.spin_number.setObjectName(u"spin_number")
        sizePolicy1.setHeightForWidth(self.spin_number.sizePolicy().hasHeightForWidth())
        self.spin_number.setSizePolicy(sizePolicy1)
        self.spin_number.setMinimum(1)
        self.spin_number.setMaximum(150)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spin_number)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.verticalSpacer)

        self.label_r_execute = QLabel(self.formLayoutWidget)
        self.label_r_execute.setObjectName(u"label_r_execute")
        sizePolicy.setHeightForWidth(self.label_r_execute.sizePolicy().hasHeightForWidth())
        self.label_r_execute.setSizePolicy(sizePolicy)
        self.label_r_execute.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_r_execute)

        self.check_execute = QCheckBox(self.formLayoutWidget)
        self.check_execute.setObjectName(u"check_execute")
        sizePolicy.setHeightForWidth(self.check_execute.sizePolicy().hasHeightForWidth())
        self.check_execute.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        self.check_execute.setFont(font1)
        self.check_execute.setLayoutDirection(Qt.LeftToRight)
        self.check_execute.setChecked(True)
        self.check_execute.setAutoRepeat(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.check_execute)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.label_execute = QLabel(self.formLayoutWidget)
        self.label_execute.setObjectName(u"label_execute")
        self.label_execute.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_execute)

        self.spin_execute = QSpinBox(self.formLayoutWidget)
        self.spin_execute.setObjectName(u"spin_execute")
        self.spin_execute.setMinimum(1)
        self.spin_execute.setMaximum(20)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.spin_execute)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(7, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.label_r_arrival = QLabel(self.formLayoutWidget)
        self.label_r_arrival.setObjectName(u"label_r_arrival")
        self.label_r_arrival.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_r_arrival)

        self.check_arrival = QCheckBox(self.formLayoutWidget)
        self.check_arrival.setObjectName(u"check_arrival")
        self.check_arrival.setFont(font1)
        self.check_arrival.setChecked(True)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.check_arrival)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(9, QFormLayout.LabelRole, self.verticalSpacer_4)

        self.label_arrival = QLabel(self.formLayoutWidget)
        self.label_arrival.setObjectName(u"label_arrival")
        self.label_arrival.setFont(font)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_arrival)

        self.spin_arrival = QSpinBox(self.formLayoutWidget)
        self.spin_arrival.setObjectName(u"spin_arrival")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.spin_arrival)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(11, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.label_algorithm = QLabel(self.formLayoutWidget)
        self.label_algorithm.setObjectName(u"label_algorithm")
        self.label_algorithm.setFont(font)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_algorithm)

        self.combo_algorithm = QComboBox(self.formLayoutWidget)
        self.combo_algorithm.setObjectName(u"combo_algorithm")
        self.combo_algorithm.setFont(font1)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.combo_algorithm)

        self.label_data = QLabel(self.formLayoutWidget)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_data)

        self.check_data = QCheckBox(self.formLayoutWidget)
        self.check_data.setObjectName(u"check_data")
        self.check_data.setEnabled(False)
        self.check_data.setFont(font1)
        self.check_data.setCheckable(True)
        self.check_data.setChecked(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.check_data)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(1, QFormLayout.LabelRole, self.verticalSpacer_6)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(90, 500, 581, 37))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_generate = QPushButton(self.horizontalLayoutWidget)
        self.button_generate.setObjectName(u"button_generate")
        self.button_generate.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_generate.sizePolicy().hasHeightForWidth())
        self.button_generate.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.button_generate)

        self.check_data.stateChanged.connect(self.enable_options)
        self.check_arrival.stateChanged.connect(self.forbid_replay)
        self.check_execute.stateChanged.connect(self.forbid_replay)
        self.spin_arrival.valueChanged.connect(self.forbid_replay)
        self.spin_execute.valueChanged.connect(self.forbid_replay)
        self.spin_number.valueChanged.connect(self.forbid_replay)

        self.button_exit = QPushButton(self.horizontalLayoutWidget)
        self.button_exit.setObjectName(u"button_exit")
        sizePolicy2.setHeightForWidth(self.button_exit.sizePolicy().hasHeightForWidth())
        self.button_exit.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.button_exit)

        MainProcesses.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainProcesses)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 29))
        MainProcesses.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainProcesses)
        self.statusbar.setObjectName(u"statusbar")
        MainProcesses.setStatusBar(self.statusbar)

        self.retranslateUi(MainProcesses)

        QMetaObject.connectSlotsByName(MainProcesses)
        self.combo_algorithm.addItem("SJF")
        self.combo_algorithm.addItem("FCFS")
        self.button_generate.clicked.connect(self.generate_clicked)
    # setupUi

    def retranslateUi(self, MainProcesses):
        MainProcesses.setWindowTitle(QCoreApplication.translate("MainProcesses", u"Generator", None))
        self.label_number.setText(QCoreApplication.translate("MainProcesses", u"Number of prcesses:", None))
        self.label_r_execute.setText(
            QCoreApplication.translate("MainProcesses", u"Random execution time for every process:", None))
        self.check_execute.setText(QCoreApplication.translate("MainProcesses", u"checked - yes", None))
        self.label_execute.setText(QCoreApplication.translate("MainProcesses", u"Range of execution time:", None))
        self.label_r_arrival.setText(
            QCoreApplication.translate("MainProcesses", u"Random arrival time for every process:", None))
        self.check_arrival.setText(QCoreApplication.translate("MainProcesses", u"checked - yes", None))
        self.label_arrival.setText(QCoreApplication.translate("MainProcesses", u"Range of arrival time:", None))
        self.label_algorithm.setText(QCoreApplication.translate("MainProcesses", u"Choose algorithm:", None))
        self.label_data.setText(QCoreApplication.translate("MainProcesses", u"Use data from previous test: ", None))
        self.check_data.setText(QCoreApplication.translate("MainProcesses", u"checked - yes", None))
        self.button_generate.setText(QCoreApplication.translate("MainProcesses", u"Generate", None))
        self.button_exit.setText(QCoreApplication.translate("MainProcesses", u"Exit", None))

        # retranslateUi

    def show_data(self, processes):
        self.dialog = QDialog()
        self.dialog.ui = Ui_DialogResult()
        self.dialog.ui.setupUi(self.dialog)
        length = len(processes) - 1
        self.dialog.ui.table.setColumnCount(4)
        # resize each column
        self.dialog.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # disable editing
        self.dialog.ui.table.verticalHeader().setVisible(False)
        self.dialog.ui.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dialog.ui.table.setRowCount(length)
        self.dialog.ui.table.setHorizontalHeaderLabels(["Process", "Arrival", "Execution", "Waiting"])
        for i in range(length):
            self.dialog.ui.table.setItem(i, 0, QTableWidgetItem(str(i)))
            self.dialog.ui.table.setItem(i, 1, QTableWidgetItem(str(processes[i].arrival)))
            self.dialog.ui.table.setItem(i, 2, QTableWidgetItem(str(processes[i].execute)))
            self.dialog.ui.table.setItem(i, 3, QTableWidgetItem(str(processes[i].waiting)))
        self.dialog.ui.label_result.setText(str(processes[-1]))
        self.dialog.ui.button_close.clicked.connect(self.dialog.close)
        self.dialog.exec()

    def generate_clicked(self):
        self.check_data.setEnabled(True)
        global processes_list
        number = self.spin_number.value()
        random_execute = self.check_execute.isChecked()
        execute = self.spin_execute.value()
        random_arrival = self.check_arrival.isChecked()
        arrival = self.spin_arrival.value()
        algorithm = self.combo_algorithm.currentText()
        if self.check_data.isChecked():
            processes = processes_list.copy()
        else:
            processes_list = process_gen.generate_processes(number, random_execute, execute, random_arrival, arrival)
            processes = processes_list.copy()
        processes = process_gen.execute_algorithm(processes, self.combo_algorithm.currentText())
        process_gen.save_test(number, random_execute, execute, random_arrival, arrival, algorithm, processes)
        self.check_data.setChecked(False)
        self.show_data(processes)

    def enable_options(self):
        if self.check_data.isChecked():
            self.spin_number.setEnabled(False)
            self.check_execute.setEnabled(False)
            self.spin_execute.setEnabled(False)
            self.check_arrival.setEnabled(False)
            self.spin_arrival.setEnabled(False)
        else:
            self.spin_number.setEnabled(True)
            self.check_execute.setEnabled(True)
            self.spin_execute.setEnabled(True)
            self.check_arrival.setEnabled(True)
            self.spin_arrival.setEnabled(True)

    def forbid_replay(self):
        self.check_data.setChecked(False)
        self.check_data.setEnabled(False)