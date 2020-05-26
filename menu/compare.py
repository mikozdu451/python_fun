from typing import List
import time
import requests
from bs4 import BeautifulSoup
import datetime
import matplotlib.pyplot as plt


def graph_creator(name):
    f = open(name, "r")
    prices = {'Taiwangun': [], 'Gunfire': [], 'Azteko': [], 'Redberet': [], 'Taniemilitaria': []}
    colors = {'Taiwangun': 'black', 'Gunfire': '#f35500', 'Azteko': '#99840e', 'Redberet': 'red', 'Taniemilitaria': 'green'}
    if f:
        savefile = name.replace(".txt", "") + "Graph.pdf"
        i = 1
        dates = []
        for line in f:
            if i in range(1, 500, 6):
                x = line[0:19]
                dates.append(x)
                i += 1
            elif i in range(2, 500, 6):
                prices['Taiwangun'].append(float(line[15:21]))
                i += 1
            elif i in range(3, 500, 6):
                prices['Gunfire'].append(float(line[15:21]))
                i += 1
            elif i in range(4, 500, 6):
                prices['Azteko'].append(float(line[15:21]))
                i += 1
            elif i in range(5, 500, 6):
                prices['Redberet'].append(float(line[15:21]))
                i += 1
            elif i in range(6, 500, 6):
                prices['Taniemilitaria'].append(float(line[15:21]))
                i += 1
        for key in prices:
            plt.plot(dates, prices[key], label=key, color=colors[key])
            plt.xticks(rotation=90)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(name.replace(".txt", ""))
        plt.legend()
        plt.tight_layout()
        plt.savefig(savefile)
        f.close()
        print("Graph created successfully!")
    else:
        print("File can't be found!")


def compare_price(holder):
    print("Waking up...")
    print("Establishing connection for all items:")
    try:
        name_file = holder[0] + ".txt"
        shop_list = ["Taiwangun     ", "Gunfire       ", "Azteko        ", "RedBeret      ", "TanieMilitaria"]
        price_list: List = []
        url1 = holder[1]
        url2 = holder[2]
        url3 = holder[3]
        url4 = holder[4]
        url5 = holder[5]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        page = requests.get(url1, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price1_convert = float(soup.find(class_="price").get_text().strip()[0:6].replace(",", "."))
        price1_convert = ("{:3.2f}".format(price1_convert))
        # print(price1_convert)
        price_list.append(price1_convert)
        print("1: Positive")
        page2 = requests.get(url2, headers=headers)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        price2_convert = float(soup2.find(class_="projector_price_value").get_text().strip()[0:6])
        price2_convert = ("{:3.2f}".format(price2_convert))
        # print(price2_convert)
        price_list.append(price2_convert)
        print("2: Positive")
        # AZTEKO
        page3 = requests.get(url3, headers=headers)
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        price3_convert = float(soup3.find(id="CenaGlownaProduktuBrutto").get_text().strip().split()[1].replace(",", "."))
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

        x = int(input("For how many secconds do you want the program to run?: "))
        y = int(input("In how many secconds do you want program to refresh? (can't be 0): "))

        if y != 0:
            print("Starting...")
            for j in range(x//y + 1):
                if j != 0:
                    print("Refreshing...")
                try:
                    if j == 0:
                        print("Searching for file...")
                    f = open(name_file)
                except FileNotFoundError:
                    print("File not found...")
                    f = open(name_file, "w+")
                    print("Creating file...")
                finally:
                    f.close()
                    if j == 0:
                        print("Opening file...")
                    f = open(name_file, "r")
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
                                        line_holder[i] = line_holder[i][0:21].replace("\n", "") + " NOCHANGE"
                                else:
                                    value = float(line_holder[i][15:21])
                                    if float(price_list[i]) > value:
                                        line_holder[i] = shop_list[i] + " " + price_list[i] + " +++"
                                    else:
                                        line_holder[i] = shop_list[i] + " " + price_list[i] + " ---"
                        else:
                            for i in range(len(shop_list)):
                                line_holder.append(shop_list[i] + " " + price_list[i])
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
                                line_holder[i] = line_holder[i].replace("\n", "") + " <--BESTPRICE"

                        f.close()
                        f = open(name_file, "a")
                        print(str(datetime.datetime.today()), file = f, flush = True)
                        for i in range(len(line_holder)):
                            print(line_holder[i].replace("\n",""), file = f, flush = True)
                        f.close()
                        time.sleep(y)
            input("Task finished succesfully! Press enter to exit ")

        else:
            input("Wrong values! Press enter and launch program again! ")

    except:
        print("Connection can't be established! Please check your internet connection!")
        input("Press enter to close program ")


def management():
    while True:
        print("Welcome to product management page")
        print("1. Check product list")
        print("2. Add product")
        print("3. Graph for product")
        print("4. Go back to menu")
        choice_manager = int(input("Number of task which you want to run: "))
        if choice_manager == 1:
            try:
                fp = open("productlist.txt", "r")
                print("\nProducts: ")
                for line in fp:
                    print(line.split()[0])
                fp.close()
                print("")
            except FileNotFoundError:
                print("No products have been added yet! Please add some using Add product option in management menu")

        elif choice_manager == 2:
            try:
                print("Opening file...")
                fp = open("productlist.txt")
            except FileNotFoundError:
                print("File not found!")
                fp = open("productlist.txt", "w+")
                print(" Creating file...")
            finally:
                fp.close()
                fp = open("productlist.txt", "a+")
                print("Please fill the first line with name of the product and rest with links to corresponding shops")
                name = input("Type in product name: ").replace(" ", "")
                tai_link = input("Taiwangun: ")
                gun_link = input("Gunfire: ")
                azt_link = input("Azteko: ")
                red_link = input("Redberet: ")
                tan_link = input("Taniemilitaria: ")
                fp.write(name+" "+tai_link+" "+gun_link+" "+azt_link+" "+red_link+" "+tan_link+"\n")
                fp.close()

        elif choice_manager == 3:
            try:
                fz = open("productlist.txt", "r")
                print("\nProducts: ")
                for line in fz:
                    print(line.split()[0])
                fz.close()
                print("")
                product_choice = input("For which product do you want to create a graph?: ")
                product_choice = product_choice +".txt"
                graph_creator(product_choice)
            except FileNotFoundError:
                print("No products have been added yet! Please add some using Add product option in management menu")

        elif choice_manager == 4:
            break

        else:
            print("Unknown command! Please try again")


def star_compare():
    try:
        fc = open("productlist.txt", "r")
        print("Which product price do you want to compare?")
        line_save = ""
        print("\nProducts: ")
        for line in fc:
            print(line.split()[0])
        fc.close()
        print("")
        choice_compare = input()
        fc = open("productlist.txt", "r")
        for line in fc:
            if choice_compare in line:
                line_save = line
        fc.close()
        line_save = line_save.split()
        compare_price(line_save)

    except FileNotFoundError:
        print("You haven't got any products yet! Add products using Manage products!")


while True:
    print("Menu")
    print("1. Start compare")
    print("2. Manage products")
    print("3. Credits")
    print("4. Help")
    print("5. Close")
    choice_menu = int(input("Number of task which you want to run: "))
    if choice_menu == 1:
        star_compare()
    elif choice_menu == 2:
        management()
    elif choice_menu == 3:
        print("""
        PRICE COMPARE ASG
        Version: 0.8
        Release date: 12.05.2020
        Author: mikozdun01/mikozdu451
        
        Thank you for using!"""
        )
    elif choice_menu == 4:
        print("""
        HELP PAGE
        Welcome to ASG PRICE COMPARE PROGRAM!
        
        To use the program properly:
        1. Make sure that the program is in a separate folder, it will generate files and you don't want those to get lost!
        2. Don't change files generated by program! It will cause problems!
        
        To start comparing product prices:
        1. Go to Manage products (2)
        2. Go to Add product
        3. Provide the name of the product which you want to add
        4. Provide links for the corresponding shops. All links MUST be filled!
        5. Go back to menu (4)
        6. Make sure you are connected to internet to compare prices!
        7. Start compare (1)
        8. Select your product from the input list
        9. If you want the product to run just once type 0 in how many seconds
           Else your program will run 1 + how many seconds / how many repeats
        10. All done! You will need to compare prices at least two times to generate proper graph
        11. From menu go to manage (2) and then to Graph (3) and select product from your product list to generate graph for your product
        """)
    elif choice_menu == 5:
        print("Shutting down...")
        break
    elif choice_menu == 69:
        print("""
          ________________    ________________________  ___   ________________ 
         /  _____/   __   \  /   _____/\_   _____/\   \/  /  /  _____/   __   \ 
        /   __  \ \____   /  \_____  \  |    __)_  \     /  /   __  \ \____   /
        \  |__\  \  /    /   /        \ |        \ /     \  \  |__\  \  /    / 
         \_____ _/ /____/   /_______ _//_______ _//___/\ _\  \_____ _/ /____/  
       """)
    else:
        print("Unknown command! Please try again")
