import bs4
from gethtml import getHtml

class parsingURL:
    def __init__(self, url):
        self.totalPage = self.totalPage(url)
        self.base_url, self.page_part, self.query_part = self.parsingURL(url)



    def returnURL(self):
         return self.totalPage, self.base_url, self.page_part, self.query_part

    def totalPage(self, url):
        return (self.get_total_pages(getHtml().get_html(url)))


    def parsingURL(self, url):
        i = 0
        for u in url:
            if u == '?':
                base_url = url[:i+1]
                temp = url[i+1:]
                break
            i += 1

        page_part = temp[:2]
        where = temp.find('&')
        query_part = temp[where :]

        return base_url, page_part, query_part


    def get_total_pages(self, html):
        soup = bs4.BeautifulSoup(html, 'lxml')
        pages = soup.find('div', class_="pagination-pages").find_all('a', class_="pagination-page")[-1].get('href')
        total_pages = pages.split('=')[1].split("&")[0]
        return int(total_pages)

if __name__ == '__main__':
    url = 'https://www.avito.ru/ekaterinburg/telefony?p=1&q=htc'
    X = parsingURL(url)
    totalPage, base_url, page_part, query_part = X.returnURL()
    print(totalPage, base_url, page_part, query_part)