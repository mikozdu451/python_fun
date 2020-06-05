from tkinter import *
from tkinter import messagebox
import sqlite3
from typing import List
import time
import requests
from bs4 import BeautifulSoup
import datetime
import re
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import filedialog
import os

root = Tk()
root.title("PriceCompare V0.8")
root.geometry("910x400")
root.iconbitmap("cart.ico")


def edit(idx):
    result = messagebox.askokcancel("Edit box",
                                    "Are you sure you want to edit product?\nIf you change the name of the products all the files with the previous name will no longer be available!")
    if result:
        conn = sqlite3.connect("product_book.db")
        # Create a cursor
        c = conn.cursor()
        c.execute("""UPDATE products SET
        name_product = :name_product,
        tg_link = :tg_link,
        gf_link = :gf_link,
        az_link = :az_link,
        rb_link = :rb_link,
        tm_link = :tm_link
        
        WHERE oid =:oid""",
                  {
                      'name_product': name_in.get(),
                      'tg_link': taiwangun_in.get(),
                      'gf_link': gunfire_in.get(),
                      'az_link': azteko_in.get(),
                      'rb_link': redberet_in.get(),
                      'tm_link': taniemilitaria_in.get(),
                      'oid': idx
                  })
        conn.commit()
        conn.close()
    else:
        return


def edit_product():
    clear_edit()
    global product_name
    global taiwangun_name
    global gunfire_name
    global redberet_name
    global azteko_name
    global taniemilitaria_name
    global name_in
    global taiwangun_in
    global gunfire_in
    global azteko_in
    global redberet_in
    global taniemilitaria_in
    global edit_button
    record_id = str(list_box.get(ANCHOR)).split()[0]
    conn = sqlite3.connect("product_book.db")
    # Create a cursor
    c = conn.cursor()
    c.execute("SELECT *, oid FROM products WHERE oid=" + record_id)
    records = c.fetchall()

    product_name = Label(root, text="Product name", pady=10)
    taiwangun_name = Label(root, text="Taiwangun", pady=10)
    gunfire_name = Label(root, text="Gunfire", pady=10)
    azteko_name = Label(root, text="Azteko", pady=10)
    redberet_name = Label(root, text="Redberet", pady=10)
    taniemilitaria_name = Label(root, text="Taniemilitaria", pady=10)
    product_name.grid(row=1, column=1)
    taiwangun_name.grid(row=2, column=1)
    gunfire_name.grid(row=3, column=1)
    azteko_name.grid(row=4, column=1)
    redberet_name.grid(row=5, column=1)
    taniemilitaria_name.grid(row=6, column=1)
    name_in = Entry(root, width=20)
    taiwangun_in = Entry(root, width=20)
    gunfire_in = Entry(root, width=20)
    azteko_in = Entry(root, width=20)
    redberet_in = Entry(root, width=20)
    taniemilitaria_in = Entry(root, width=20)
    name_in.grid(row=1, column=2)
    taiwangun_in.grid(row=2, column=2)
    gunfire_in.grid(row=3, column=2)
    azteko_in.grid(row=4, column=2)
    redberet_in.grid(row=5, column=2)
    taniemilitaria_in.grid(row=6, column=2)
    edit_button = Button(root, text="Edit product", command=lambda: edit(record_id), bg="green")
    edit_button.grid(row=3, column=3, ipady=20, rowspan=2)
    for item in records:
        name_in.insert(0, item[0])
        taiwangun_in.insert(0, item[1])
        gunfire_in.insert(0, item[2])
        azteko_in.insert(0, item[3])
        redberet_in.insert(0, item[4])
        taniemilitaria_in.insert(0, item[5])
    conn.close()


def remove_product():
    result = messagebox.askyesno("Delete", "Are you sure you want to delete item: {}?".format(
        str(list_box.get(ANCHOR)).split()[-1]))
    if result:
        to_delete = str(list_box.get(ANCHOR)).split()[0]

        # create a database
        conn = sqlite3.connect("product_book.db")
        # create cursor
        c = conn.cursor()

        c.execute("DELETE from products WHERE oid=" + to_delete)

        # commit
        conn.commit()
        # close
        conn.close()
        show()
    else:
        return


def show():
    global list_box
    list_box.delete(0, END)
    conn = sqlite3.connect("product_book.db")
    # Create a cursor
    c = conn.cursor()
    x = 1
    c.execute("SELECT *, oid FROM products")
    records = c.fetchall()
    for record in records:
        list_box.insert(x, str(record[-1])+"            "+record[0])
    list_box.grid(row=1, column=4, rowspan=9000, columnspan=2)
    conn.close()


def submit():
    if 'gunfire' in gunfire_in.get() and 'taiwangun' in taiwangun_in.get() and 'azteko' in azteko_in.get() and 'redberet' in redberet_in.get() and 'taniemilitaria' in taniemilitaria_in.get() and name_in.get():
        # Create a database
        conn = sqlite3.connect("product_book.db")
        # Create a cursor
        c = conn.cursor()
        # Create a table
        try:
            c.execute("""CREATE TABLE products(
                    name_product text,
                    tg_link text,
                    gf_link text,
                    az_link text,
                    rb_link text,
                    tm_link text
                    )""")
        except sqlite3.OperationalError:
            pass

        # Add to table
        c.execute("INSERT INTO products VALUES (:name_product, :tg_link, :gf_link, :az_link, :rb_link, :tm_link)",

                  {
                      'name_product': name_in.get(),
                      'tg_link': taiwangun_in.get(),
                      'gf_link': gunfire_in.get(),
                      'az_link': azteko_in.get(),
                      'rb_link': redberet_in.get(),
                      'tm_link': taniemilitaria_in.get(),
                  })

        # Commit
        conn.commit()
        # Close
        conn.close()
        messagebox.showinfo("Process finished", "Product added to database successfully!")
        name_in.delete(0, END)
        taiwangun_in.delete(0, END)
        gunfire_in.delete(0, END)
        azteko_in.delete(0, END)
        redberet_in.delete(0, END)
        taniemilitaria_in.delete(0, END)
        show()
    else:
        messagebox.showinfo("Warning!", "Wrong arguments! Makes sure you filled ALL lines properly")


def add_product():
    global product_name
    global taiwangun_name
    global gunfire_name
    global redberet_name
    global azteko_name
    global taniemilitaria_name
    global name_in
    global taiwangun_in
    global gunfire_in
    global azteko_in
    global redberet_in
    global taniemilitaria_in
    global submit_button
    clear_edit()
    product_name = Label(root, text="Product name", pady=10)
    taiwangun_name = Label(root, text="Taiwangun", pady=10)
    gunfire_name = Label(root, text="Gunfire", pady=10)
    azteko_name = Label(root, text="Azteko", pady=10)
    redberet_name = Label(root, text="Redberet", pady=10)
    taniemilitaria_name = Label(root, text="Taniemilitaria", pady=10)
    product_name.grid(row=1, column=1)
    taiwangun_name.grid(row=2, column=1)
    gunfire_name.grid(row=3, column=1)
    azteko_name.grid(row=4, column=1)
    redberet_name.grid(row=5, column=1)
    taniemilitaria_name.grid(row=6, column=1)
    name_in = Entry(root, width=20)
    taiwangun_in = Entry(root, width=20)
    gunfire_in = Entry(root, width=20)
    azteko_in = Entry(root, width=20)
    redberet_in = Entry(root, width=20)
    taniemilitaria_in = Entry(root, width=20)
    name_in.grid(row=1, column=2)
    taiwangun_in.grid(row=2, column=2)
    gunfire_in.grid(row=3, column=2)
    azteko_in.grid(row=4, column=2)
    redberet_in.grid(row=5, column=2)
    taniemilitaria_in.grid(row=6, column=2)
    submit_button = Button(root, text="Submit product", command=submit, bg="green")
    submit_button.grid(row=3, column=3, ipady=20, rowspan=2)


def clear():
    button_1.destroy()
    button_2.destroy()
    button_3.destroy()
    menu_label.destroy()
    product_name.destroy()
    taiwangun_name.destroy()
    gunfire_name.destroy()
    azteko_name.destroy()
    redberet_name.destroy()
    taniemilitaria_name.destroy()
    name_in.destroy()
    taiwangun_in.destroy()
    gunfire_in.destroy()
    azteko_in.destroy()
    redberet_in.destroy()
    taniemilitaria_in.destroy()
    submit_button.destroy()
    edit_button.destroy()


def clear_edit():
    product_name.destroy()
    taiwangun_name.destroy()
    gunfire_name.destroy()
    azteko_name.destroy()
    redberet_name.destroy()
    taniemilitaria_name.destroy()
    name_in.destroy()
    taiwangun_in.destroy()
    gunfire_in.destroy()
    azteko_in.destroy()
    redberet_in.destroy()
    taniemilitaria_in.destroy()
    submit_button.destroy()
    edit_button.destroy()


def start_compare():
    record_id = str(list_box.get(ANCHOR)).split()[0]
    # print(record_id)
    # create a database
    conn = sqlite3.connect("product_book.db")
    # create cursor
    c = conn.cursor()

    c.execute("SELECT *, oid FROM products WHERE oid=" + record_id)
    holder = c.fetchall()
    # commit
    # print(holder)
    conn.commit()
    # close
    conn.close()

    # print("Waking up...")
    # print("Establishing connection for all items:")
    try:
        name_file = holder[0][0] + ".txt"
        shop_list = ["Taiwangun     ", "Gunfire       ", "Azteko        ", "RedBeret      ", "TanieMilitaria"]
        price_list: List = []
        url1 = holder[0][1]
        url2 = holder[0][2]
        url3 = holder[0][3]
        url4 = holder[0][4]
        url5 = holder[0][5]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        page = requests.get(url1, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price1_convert = soup.find(class_="price").get_text().strip().replace(",", ".")
        price1_convert = float(re.sub("[^0-9^.]", "", price1_convert))
        price1_convert = ("{:3.2f}".format(price1_convert))
        # print(price1_convert)
        price_list.append(price1_convert)
        # print("1: Positive")
        page2 = requests.get(url2, headers=headers)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        price2_convert = float(soup2.find(class_="projector_price_value").get_text().strip().split()[0].replace(",", "."))
        price2_convert = ("{:3.2f}".format(price2_convert))
        # print(price2_convert)
        price_list.append(price2_convert)
        # print("2: Positive")
        # AZTEKO
        page3 = requests.get(url3, headers=headers)
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        price3_convert = float(soup3.find(id="CenaGlownaProduktuBrutto").get_text().strip().split()[1].replace(",", "."))
        price3_convert = ("{:3.2f}".format(price3_convert))
        # print(price3_convert)
        price_list.append(price3_convert)
        # print("3: Positive")
        # RED
        page4 = requests.get(url4, headers=headers)
        soup4 = BeautifulSoup(page4.content, 'html.parser')
        price4_1 = soup4.find(class_="price_1").get_text().replace(",", ".")
        price4_2 = soup4.find(class_="price_2").get_text()
        price4_convert = float(price4_1 + price4_2)
        price4_convert = "{:3.2f}".format(price4_convert)
        price_list.append(price4_convert)
        # print("4: Positive")
        # TANIE
        page5 = requests.get(url5, headers=headers)
        soup5 = BeautifulSoup(page5.content, 'html.parser')
        price5_convert = float(soup5.find(class_="box-product-price-netto").get_text().split()[0].replace(",", "."))
        # print(price5_convert)
        price5_convert = ("{:3.2f}".format(price5_convert))
        price_list.append(price5_convert)
        # print("5: Positive")
        # print("Starting...")
        try:

            # print("Searching for file...")
            f = open(name_file)
        except FileNotFoundError:
            # print("File not found...")
            f = open(name_file, "w+")
            # print("Creating file...")
        finally:
            f.close()
            # print("Opening file...")
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
                print(str(datetime.datetime.today()), file=f, flush=True)
                for i in range(len(line_holder)):
                    print(line_holder[i].replace("\n", ""), file=f, flush=True)
                f.close()
                messagebox.showinfo("Compare info", "Comparing prices finished")
    except:
        messagebox.showerror("Connection error", "Unable to compare product!\nCheck your internet connection or links to products")
        return


def generate_report():
    name = str(list_box.get(ANCHOR)).split()[1]+".txt"
    f = open(name, "r")
    prices = {'Taiwangun': [], 'Gunfire': [], 'Azteko': [], 'Redberet': [], 'Taniemilitaria': []}
    colors = {'Taiwangun': 'black', 'Gunfire': '#f35500', 'Azteko': '#99840e', 'Redberet': 'red', 'Taniemilitaria': 'green'}
    if f:
        savefile = name.replace(".txt", "") + "Graph.jpg"
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
        plt.cla()
        f.close()
        messagebox.showinfo("Report generator", "Report generated successfully for product: {}!".format(str(list_box.get(ANCHOR)).split()[1]))
        # print("Graph created successfully!")
    else:
        # print("File can't be found!")
        messagebox.showerror("Report generator", "Program wasn't able to generate report!\nPlease check if you had compared prices for product: {}".format(str(list_box.get(ANCHOR)).split()[1]))


def display_report():
    global photo
    global img
    product_name_display = str(list_box.get(ANCHOR)).split()[1] + "Graph.jpg"
    img = ImageTk.PhotoImage(Image.open(product_name_display).resize((440, 370), Image.ANTIALIAS))
    photo = Label(master=root, image=img)
    photo.grid(row=1, column=1, columnspan=3, rowspan=999)
    # product_name_display = str(list_box.get(ANCHOR)).split()[1] + "Graph.jpg"
    # my_canvas = Canvas(root, width=440, height=370)
    # my_canvas.grid(row=1, column=1, columnspan=3, rowspan=999)
    # img = ImageTk.PhotoImage(Image.open(product_name_display))
    # photo = Label(root, image=img)
    # photo.grid(row=1, column=1, columnspan=3, rowspan=999)

def send_report():
    return


def start_click():
    global menu_label
    global button_1
    global button_2
    global button_3
    global button_4
    clear()
    products_label = Label(root, text="Compare menu", width=22)
    products_label.grid(row=0, column=0)
    button_1 = Button(root, text="Start compare", width=21, pady=10, command=start_compare)
    button_1.grid(row=1, column=0)
    button_2 = Button(root, text="Generate report", width=21, pady=10, command=generate_report)
    button_2.grid(row=2, column=0)
    button_3 = Button(root, text="Display report", width=21, pady=10, command=display_report)
    button_3.grid(row=3, column=0)
    button_4 = Button(root, text="Send report", width=21, pady=10, command=send_report)
    button_4.grid(row=4, column=0)
    show()


def manage_click():
    global menu_label
    global button_1
    global button_2
    global button_3

    clear()
    menu_label = Label(root, text="Manage", width=22)
    menu_label.grid(row=0, column=0)
    button_1 = Button(root, text="Add product", width=21, pady=10, command=add_product)
    button_1.grid(row=1, column=0)
    button_2 = Button(root, text="Remove product", width=21, pady=10, command=remove_product)
    button_2.grid(row=2, column=0)
    button_3 = Button(root, text="Edict product", width=21, pady=10, command=edit_product)
    button_3.grid(row=3, column=0)
    show()


def help_click():
    clear()


def set_click():
    clear()


# Main menu
menu_label = Label(root, text="Main menu", width=22)
menu_label.grid(row=0, column=0)
button_start = Button(root, text="Start compare", width=20, command=start_click)
button_start.grid(row=0, column=1)
manage_button = Button(root, text="Manage products", width=20, command=manage_click)
manage_button.grid(row=0, column=2)
help_button = Button(root, text="Help", width=20, command=help_click)
help_button.grid(row=0, column=3)
settings_button = Button(root, text="Settings", width=20, command=set_click)
settings_button.grid(row=0, column=4)
exit_button = Button(root, text="Exit", command=root.quit, width=20)
exit_button.grid(row=0, column=5)
# Left Panel Buttons
button_1 = Button(root, text="button1")
button_2 = Button(root, text="button2")
button_3 = Button(root, text="button3")
button_4 = Button(root, text="button4")
# Shop name labels
product_name = Label(root, text="Product name", pady=10)
taiwangun_name = Label(root, text="Taiwangun", pady=10)
gunfire_name = Label(root, text="Gunfire", pady=10)
azteko_name = Label(root, text="Azteko", pady=10)
redberet_name = Label(root, text="Redberet", pady=10)
taniemilitaria_name = Label(root, text="Taniemilitaria", pady=10)
# Shop add entries
name_in = Entry(root, width=20)
taiwangun_in = Entry(root, width=20)
gunfire_in = Entry(root, width=20)
azteko_in = Entry(root, width=20)
redberet_in = Entry(root, width=20)
taniemilitaria_in = Entry(root, width=20)
submit_button = Button(root, text="Submit product", command=submit, bg="green")
# Text box
list_box = Listbox(root, width=50, height=100, selectmode=SINGLE, bg="#cccccc")
list_box.grid(row=1, column=4, rowspan=9000, columnspan=2)
# Edit button
edit_button = Button(root, text="Edit product", command=submit, bg="green")
# Image
img = ImageTk.PhotoImage(Image.open("cart.ico").resize((440, 370), Image.ANTIALIAS))
photo = Label(master=root, image=img)

show()
root.mainloop()
