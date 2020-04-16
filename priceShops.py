from typing import List
import time
import requests
from bs4 import BeautifulSoup
import datetime
import os







print("Waking up...")
print("Establishing connection for all items:")
#
shop_list = ["Taiwangun     ", "Gunfire       ", "Azteko        ", "RedBeret      ", "TanieMilitaria"]
price_list: List = []
url = "https://www.taiwangun.com/elektryczne/cm-028-cyma"
url2 = 'https://gunfire.com/pl/products/replika-karabinka-cm028-1144793020.html'
url3 = 'https://azteko.pl/cyma-replika-karabinka-cm028-p-22470.html'
url4 = 'http://redberet.pl/p/59/1152243676/cyma-replika-ak47-cm028-seria-ak-elektryczne-repliki-asg-airsoft-guns.html'
url5 = 'https://www.taniemilitaria.pl/pl,ak-47-cm028-cyma,0,5,6,7,68.html#.XoOzcYgzaUk'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
# TG
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
price1_convert = float(soup.find(class_="price").get_text().strip()[0:6].replace(",", "."))
#price1_convert = price.strip()[0:6]
#price1_convert = float((price1_convert.replace(",", ".")))
price1_convert = ("{:3.2f}".format(price1_convert))
# print(price1_convert)
price_list.append(price1_convert)
print("1: Positive")
# GF
page2 = requests.get(url2, headers=headers)
soup2 = BeautifulSoup(page2.content, 'html.parser')
price2_convert = float(soup2.find(class_="projector_price_value").get_text().strip()[0:6])
#price2_convert = float(price2.strip()[0:6])
price2_convert = ("{:3.2f}".format(price2_convert))
# print(price2_convert)
price_list.append(price2_convert)
print("2: Positive")
# AZTEKO
page3 = requests.get(url3, headers=headers)
soup3 = BeautifulSoup(page3.content, 'html.parser')
price3_convert = float(soup3.find(id="CenaGlownaProduktuBrutto").get_text().strip().split()[1].replace(",", "."))
# print(price3)
#price3_convert = float(price3.replace(",", "."))
price3_convert = ("{:3.2f}".format(price3_convert))
# print(price3_convert)
price_list.append(price3_convert)
print("3: Positive")
# RED
page4 = requests.get(url4, headers=headers)
soup4 = BeautifulSoup(page4.content, 'html.parser')
price4_1 = soup4.find(class_="price_1").get_text().replace(",", ".")
price4_2 = soup4.find(class_="price_2").get_text()
price4_convert = float(price4_1 + price4_2)
price4_convert = "{:3.2f}".format(price4_convert)
# print(price4_convert)
price_list.append(price4_convert)
print("4: Positive")
# TANIE
page5 = requests.get(url5, headers=headers)
soup5 = BeautifulSoup(page5.content, 'html.parser')
price5_convert = float(soup5.find(class_="box-product-price-netto").get_text()[0:6].replace(",", "."))
# print(price5_convert)
price5_convert = ("{:3.2f}".format(price5_convert))
price_list.append(price5_convert)
print("5: Positive")

os.system('cls')

print("\nCYMA 028 PRICE COMPARE V0.1")
print("̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿\n")

x = int(input("For how many secconds do you want the program to run?: "))
y = int(input("In how many secconds do you want program to refresh?: "))

if y != 0:
    print("Starting...")
    for j in range(x//y):
        if j != 0:
            print("Refreshing...")
        try:
            if j == 0:
                print("Searching for file...")
            f = open("priceCMShops.txt")
        except FileNotFoundError:
            print("File not found...")
            f = open("priceCMShops.txt", "w+")
            print("Creating file...")
        finally:
            f.close()
            if j == 0:
                print("Opening file...")
            f = open("priceCMShops.txt", "r")
            if f:
                line_holder = []
                i = 1
                for line in f:
                    if i in range(1, 500, 6):
                        line_holder = []
                        i += 1
                    else:
                        line_holder.append(line)
                        i += 1

                # print(line_holder)
                if line_holder:
                    for i in range(len(line_holder)):
                        # print(line_holder[i])
                        if str(price_list[i]) in line_holder[i]:
                            if "NOCHANGE" not in line_holder[i]:
                                line_holder[i] = line_holder[i][0:21].replace("\n", "") + " NOCHANGE\n"
                        else:
                            value = float(line_holder[i][15:21])
                            if float(price_list[i]) > value:
                                line_holder[i] = shop_list[i] + " " + price_list[i] + " +++\n"
                            else:
                                line_holder[i] = shop_list[i] + " " + price_list[i] + " ---\n"
                else:
                    for i in range(len(shop_list)):
                        line_holder.append(shop_list[i] + " " + price_list[i] + "\n")
                # print(line_holder)
                best_price = 0
                for i in range(len(line_holder)):
                    if best_price == 0:
                        best_price = line_holder[i][15:21]
                    else:
                        if price_list[i] < best_price:
                            best_price = price_list[i]

                for i in range(len(line_holder)):
                    line_holder[i] = line_holder[i].replace(" <--BESTPRICE", "")
                    if str(best_price) in line_holder[i]:
                        line_holder[i] = line_holder[i].replace("\n", "") + " <--BESTPRICE\n"

                f.close()
                f = open("priceCMShops.txt", "a")
                f.write(str(datetime.datetime.today()) + "\n")
                for i in range(len(line_holder)):
                    f.write(line_holder[i])
                f.close()
                time.sleep(y)
    input("Task finished succesfully! Press enter to exit ")

else:
    input("Wrong values! Press enter and launch program again! ")
