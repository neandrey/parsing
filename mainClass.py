import sys
from PyQt5.QtWidgets import QApplication
import dataDB
from avito import avitoParsing
from qtMainWind import Example

class MainClass:
    def __init__(self, url, base_url, page_part, query_part, nameDB):
        self.main(url, base_url, page_part, query_part, nameDB)


    def main(self, url, base_url, page_part, query_part, nameDB):
        cur, db = dataDB.connectDB(nameDB)
        avitoParsing(url, base_url, page_part, query_part, cur, db)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    url = 'https://www.avito.ru/ekaterinburg/telefony?p=1&q=htc'
    base_url = 'https://www.avito.ru/ekaterinburg/telefony?'
    page_part = 'p='
    query_part = '&q=htc'
    nameDB = 'avitoDB'

    MainClass(url=url, base_url=base_url, page_part=page_part, query_part=query_part, nameDB = nameDB)
    ex=Example()
    sys.exit(app.exec_())