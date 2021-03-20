import requests
from bs4 import BeautifulSoup

list_of_prices = list()

for i in range(10):
    url = 'https://steamcommunity.com/market/search?appid=730'
    par = {'p': i}
    req = requests.get(url, params=par)
    soup = BeautifulSoup(req.text, 'html.parser')
    for j in range(7):
        product = soup.find_all('div')[j].get_text()
        price = soup.find_all(class_='market_listing_price_listings_block')[j].get_text()
        price = price.replace(" ", "")
        list_of_prices.append([product, price])

with open('prices.csv', 'w') as f_out:
    for i in list_of_prices:
        i = str(i)
        i = i.replace("\'", '')
        i = i.replace('[', '')
        i = i.replace(']', '')
        f_out.write(i + '\n')

