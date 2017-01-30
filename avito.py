import requests
from bs4 import BeautifulSoup
import csv
import dataDB

#m = dataDB.connectDB(data='avitoDB')
#---------------------------------------
def get_html(url):
    r = requests.get(url)
    return r.text
#----------------------------------------
def get_totoal_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_="pagination-pages").find_all('a', class_="pagination-page")[-1].get('href')
    total_pages = pages.split('=')[1].split("&")[0]

    return int(total_pages)
#-----------------------------------------
def write_table(data):
    m = dataDB.connectDB(data='avitoDB')
    dataDB.insertTable(*m, **data)
    dataDB.closeDB(*m)
#------------------------------------------
def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
                         data['price'],
                         data['url'],
                         data['metro']
                         ))
#------------------------------------------
def get_page_date(html):
    soup = BeautifulSoup(html, 'lxml')
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
            except:
                price = ''
            try:
                metro = ad.find('div', class_='data').find_all('p')[-1].text.strip()
            except:
                metro = ''

            data = {'title': title,
                    'price': price,
                    'metro': metro,
                    'url': url
                    }

            #write_csv(data)
            write_table(data)

        else:
            continue

  #  dataDB.closeDB(*m)
#-----------------------------------------------------------------
def main():
    url = 'https://www.avito.ru/ekaterinburg/telefony?p=1&q=htc'
    base_url = 'https://www.avito.ru/ekaterinburg/telefony?'
    page_part = 'p='
    query_part = '&q=htc'

    total_pages = get_totoal_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i) + query_part
        html = get_html(url_gen)
        get_page_date(html)
#----------------------------------------------------------------
if __name__ == '__main__':
    main()