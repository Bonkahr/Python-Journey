# from PyQt6.QtGui import
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
# from PyQt6.QtCore import *

import sys


class MainWindow(QMainWindow):
    def __int__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle("My First App")
        button = QPushButton('Press Here')

        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = QWidget()
window.show()

app.exec()


