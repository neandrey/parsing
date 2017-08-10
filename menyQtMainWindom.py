from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

class MenyQtMainWindow():
    '''
    Создание меню главного окна приложения 
    для вывода данных пользователю.
    '''
    def __init__(self):
        self.Exit()
        self.Open()


    def Exit(self):
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitWindow)


        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)



    def Open(self):
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.openFileDialog)


        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        toolbar = self.addToolBar('Open')
        toolbar.addAction(openFile)
