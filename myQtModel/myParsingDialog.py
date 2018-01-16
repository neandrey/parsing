import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QGridLayout, QApplication, QPushButton


class MyParsingDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.InitDialog()


    def InitDialog(self):
        self.title = QLabel('url:')
        self.titleEdit = QLineEdit()
        self.button = QPushButton('Ok', self)
        self.button.clicked.connect(self.resiveData)


        grid = QGridLayout()
        grid.setSpacing(10)


        grid.addWidget(self.title, 1, 0)
        grid.addWidget(self.titleEdit, 1, 1)
        grid.addWidget(self.button, 2, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('Review')
        self.show()

    @pyqtSlot(name = 'resiveData')
    def resiveData(self):
        hello = self.titleEdit.text()
        return hello

    @pyqtSlot(name = 'QuitWindows')
    def closeWindow(self):
        self.close()


#----------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyParsingDialog()
    sys.exit(app.exec_())

