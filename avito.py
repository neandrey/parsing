import requests
import bs4
import csv
import dataDB

#---------------------------------------
def get_html(url):
    r = requests.get(url)
    return r.text
#----------------------------------------
def get_total_pages(html):
    soup = bs4.BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_="pagination-pages").find_all('a', class_="pagination-page")[-1].get('href')
    total_pages = pages.split('=')[1].split("&")[0]

    return int(total_pages)
#-----------------------------------------
def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
                         data['price'],
                         data['url'],
                         data['metro']
                         ))
#------------------------------------------
def get_page_date(html, cur, db):
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
                    #print(price)
                    price = price[:-1]
                    price = (''.join(price))
                    if price == price.isdigit():
                        price = int(price)
                    else:
                        price = None
                    #print(price)

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

            #write_csv(data)
            dataDB.insertTable(cur, db ,**data)

        else:
            continue
#-----------------------------------------------------------------
def main(cur, db):
    url = 'https://www.avito.ru/ekaterinburg/telefony?p=1&q=htc'
    base_url = 'https://www.avito.ru/ekaterinburg/telefony?'
    page_part = 'p='
    query_part = '&q=htc'

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i) + query_part
        html = get_html(url_gen)
        get_page_date(html, cur, db)
#----------------------------------------------------------------
if __name__ == '__main__':
    m = dataDB.connectDB(data='avitoDB')
    main(*m)
    dataDB.closeDB(*m)