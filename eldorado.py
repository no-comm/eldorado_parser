import requests
from bs4 import BeautifulSoup as bs
import config
def collect(name):
    response = requests.get(f'https://www.eldorado.ru/search/catalog.php?q={name}&utf', cookies=config.cookies, headers=config.headers)
    soup = bs(response.text, "lxml")
    prices = soup.find_all('span', class_="xS ES")
    names = soup.find_all("a", class_="FF")
    price = []
    name = []
    for i in prices:
        price.append(i.text.replace("\xa0", " "))
    for i in names:
        name.append(i.text)
    list = []
    list.append(price)
    list.append(name)
    return list