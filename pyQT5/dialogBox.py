import sys
from PyQt6.QtWidgets import QApplication, QFormLayout, QLineEdit, QDialog, \
    QVBoxLayout, QDialogButtonBox


class Dialog(QDialog):
    """Dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Job:', QLineEdit())
        formLayout.addRow('Hobbies:', QLineEdit())
        dlgLayout.addLayout(formLayout)
        button = QDialogButtonBox()
        # button.setStandardButtons(
        #     QDialogButtonBox.clear() | QDialogButtonBox.Ok)
        dlgLayout.addWidget(button)
        self.setLayout(dlgLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec())
