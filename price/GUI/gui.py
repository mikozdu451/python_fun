from tkinter import *

root = Tk()
root.title("PriceCompare V0.8")
root.geometry("910x400")
root.iconbitmap("cart.ico")


def add_product():
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


def start_click():
    global menu_label
    global button_1
    global button_2
    global button_3
    clear()
    products_label = Label(root, text="Compare menu", width=22)
    products_label.grid(row=0, column=0)
    list_of_products = Listbox()


def manage_click():
    global menu_label
    global button_1
    global button_2
    global button_3

    clear()
    menu_label = Label(root, text="Manage", width=22)
    menu_label.grid(row=0, column=0)
    button_1 = Button(root, text="Product list", width=21, pady=10,)
    button_1.grid(row=1, column=0)
    button_2 = Button(root, text="Add product", width=21, pady=10, command=add_product)
    button_2.grid(row=2, column=0)
    button_3 = Button(root, text="Remove product", width=21, pady=10,)
    button_3.grid(row=3, column=0)


# Main menu
menu_label = Label(root, text="Main menu", width=22)
menu_label.grid(row=0, column=0)
button_start = Button(root, text="Start compare", width=20, command=start_click)
button_start.grid(row=0, column=1)
manage_button = Button(root, text="Manage products", width=20, command=manage_click)
manage_button.grid(row=0, column=2)
help_button = Button(root, text="Help", width=20)
help_button.grid(row=0, column=3)
credits_button = Button(root, text="Credits", width=20)
credits_button.grid(row=0, column=4)
exit_button = Button(root, text="Exit", command=root.quit, width=20)
exit_button.grid(row=0, column=5)
# Left Panel Buttons
button_1 = Button(root, text="button1")
button_2 = Button(root, text="button2")
button_3 = Button(root, text="button3")
# Shop name labels
product_name = Label(root, text="Product name", pady=10)
taiwangun_name = Label(root, text="Taiwangun", pady=10)
gunfire_name = Label(root, text="Gunfire", pady=10)
azteko_name = Label(root, text="Azteko", pady=10)
redberet_name = Label(root, text="Redberet", pady=10)
taniemilitaria_name = Label(root, text="Taniemilitaria", pady=10)

root.mainloop()
