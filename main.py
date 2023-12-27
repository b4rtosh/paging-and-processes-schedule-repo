
from pages import Ui_MainPages
from processes import Ui_MainProcesses
from menu import Ui_MainMenu
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

class MainPages (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainPages()
        self.ui.setupUi(self)
        self.ui.button_close.clicked.connect(self.open_menu)

    def open_menu(self):
        self.menu = MainMenu()
        self.menu.show()
        self.close()


class MainProcesses (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainProcesses()
        self.ui.setupUi(self)
        self.ui.button_exit.clicked.connect(self.open_menu)

    def open_menu(self):
        self.menu = MainMenu()
        self.menu.show()
        self.close()

class MainMenu (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.button_paging.clicked.connect(self.open_pages)
        self.ui.button_processes.clicked.connect(self.open_processes)

    def open_pages(self):
        self.pages = MainPages()
        self.pages.show()
        self.close()

    def open_processes(self):
        self.processes = MainProcesses()
        self.processes.show()
        self.close()


if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())
