import requests
from bs4 import BeautifulSoup
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
url4 = 'http://redberet.pl/p/159/1152301993/cyma-replika-cm125-tan-pistolety-elektryczne-repliki-asg-airsoft-guns.html'
page4 = requests.get(url4, headers=headers)
soup4 = BeautifulSoup(page4.content, 'html.parser')
price4_1 = soup4.find(class_="price_1").get_text().replace(",", ".")
price4_2 = soup4.find(class_="price_2").get_text()
price4_convert = float(price4_1 + price4_2)
price4_convert = "{:3.2f}".format(price4_convert)
print(price4_convert)
