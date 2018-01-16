import sys
from parsingurl import parsingURL
from gethtml import getHtml
from avito import avitoParsing



class Main:
    def __init__(self, url):
        self.parsing = parsingURL(url).returnURL()
        self.avito = avitoParsing()
        self.mainFunc()



    def mainFunc(self):
        for i in range(1, self.parsing[0]):
            html = self.get_html_arg(i)
            self.avito.get_page_date(html)

    def get_html_arg(self, iter):
        url_gen = self.parsing[1] + self.parsing[2] + str(iter) + self.parsing[3]
        return getHtml().get_html(url_gen)


if __name__ == '__main__':
    url = 'https://www.avito.ru/ekaterinburg/telefony?p=1&q=htc'
    main = Main(url)