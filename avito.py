import bs4
import csv


class avitoParsing():

    def get_page_date(self, html):
        soup = bs4.BeautifulSoup(html, 'lxml')
        ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
        for ad in ads:
        # title url, price, metro
            name = ad.find('div', class_='description').find('h3').text.strip().lower()

            if 'htc' in name:
                try:
                    title = ad.find('div', class_='description').find('h3').text.strip()
                except:
                    title = ''
                try:
                    url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
                except:
                    url = ''
                try:
                    price = ad.find('div', class_='about').text.strip()
                    if price == '':
                        price = None
                    else:
                        price = price.split(' ')
                        price = price[:-1]
                        price = (''.join(price))
                        if price == price.isdigit():
                            price = int(price)
                        else:
                            price = None

                except price:
                    price = None

                try:
                    metro = ad.find('div', class_='data').find_all('p')[-1].text.strip()
                except:
                    metro = ''

                data = {'title': title,
                        'price': price,
                        'metro': metro,
                        'url': url
                        }
                print(data)

            else:
                continue

if __name__ == '__main__':
    pass
    #avito = avitoParsing(url)
    # url = 'https://www.avito.ru/ekaterinburg/telefony?p=1&q=htc'


    # base_url = 'https://www.avito.ru/ekaterinburg/telefony?'
    # page_part = 'p='
    # query_part = '&q=htc'
    #
    # total_pages = avitoParsing.get_total_pages(avitoParsing.get_html(url))
    #
    # for i in range(1, total_pages):
    #     url_gen = base_url + page_part + str(i) + query_part
    #     html = avitoParsing.get_html(url_gen)
    #     avitoParsing.write_csv()
 # def write_csv(self, data):
    #     with open('avito.csv', 'a') as f:
    #         writer = csv.writer(f)
    #         writer.writerow((data['title'],
    #                      data['price'],
    #                      data['url'],
    #                      data['metro']))
    #