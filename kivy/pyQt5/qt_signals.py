from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt6.QtCore import Qt

import sys


class MainWindow(QMainWindow):

    def __int__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self):
        print('Button clicked')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()

    app.exec()
