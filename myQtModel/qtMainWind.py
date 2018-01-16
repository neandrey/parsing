import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication

from myQtModel.menyQtMainWindom import MenyQtMainWindow
from myQtModel.myDialogWindow import MyDialogWindow


class Example(QMainWindow):
    '''
    Создание главного окна приложения 
    для вывода данных пользователю.
    '''
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        '''
        Инициализация главного окна.
        '''
        #MenyQtMainWindow.Open(self)
        MenyQtMainWindow.Exit(self)


        #ex = MyTable(data, 5, 3)
        #self.setCentralWidget(ex)


        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('GridWindow')
        self.show()

    @pyqtSlot(name='Exit')
    def exitWindow(self):
        MyDialogWindow.exitDialog(self)

    @pyqtSlot(name='Open')
    def openFileDialog(self):
        MyDialogWindow.openDialog(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
