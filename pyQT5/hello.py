import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# for consistency camelCase will be used
# Creating Instance of QApplication
app = QApplication(sys.argv)

# Creating instance of GUI APP
window = QWidget()
window.setWindowTitle('PyQt5 First App')
window.setGeometry(0, 0, 640, 640)
window.move(0, 0)
helloMsg = QLabel('<h1>Hello There</h1>', parent=window)
helloMsg.move(15, 15)
welcomeMsg = QLabel('<h2>Welcome to pyQT5</h2>', parent=window)
welcomeMsg.move(0, 40)

# show app GUI
window.show()

# Run app event loop (main loop)
sys.exit(app.exec_())

