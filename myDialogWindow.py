from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox, qApp, QFileDialog


class MyDialogWindow():

    trigger = pyqtSignal()

    def __init__(self):
        self.exitDialog()

    def exitDialog(self):
        """
        Подтверждение выхода из приложения.
        """
        reply = QMessageBox.question(self,
                                     'Message',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes |  QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            qApp.quit()
        #else:

    def openDialog(self):
        """
        Открыти файлов. 
        """
        pass
        #reply = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        #f = open(reply, 'r')





