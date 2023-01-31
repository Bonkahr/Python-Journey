from PyQt6 import QtWidgets

# needed for access to command line args.
import sys

# application instance only needed once
# if no command line args needed - QApplication([]) works too
app = QtWidgets.QApplication(sys.argv)

# creating a QT widget
window = QtWidgets.QMainWindow()
window.setWindowTitle('QT6 App 1')
# window = QtWidgets.QPushButton('Log In')
window.show()  # windows are hidden by default. Needed to show the window.

# starting the event loop
app.exec()
