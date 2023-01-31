import sys

from PyQt6 import QtWidgets, QtCore


class MainWindow(QtWidgets.QMainWindow):

    def __int__(self):
        super().__init__()

        self.setWindowTitle("App Main Window")
        self.setFixedSize(800, 800)
        button = QtWidgets.QPushButton('Like me?')
        # button.setText('Hello')

        # setting the central widget of the window
        self.setCentralWidget(button)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
