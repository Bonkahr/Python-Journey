import sys

from PyQt5.QtWidgets import QApplication, QFormLayout, QLineEdit, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QFormLayout')
layout = QFormLayout()
name = layout.addRow('Name', QLineEdit())
age = layout.addRow('Age', QLineEdit())
job = layout.addRow('Job', QLineEdit())
hobbies = layout.addRow('Hobbies', QLineEdit())
window.setLayout(layout)
window.show()
# print(name, age, job, hobbies)
sys.exit(app.exec_())
