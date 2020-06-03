from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("PriceCompare V0.8")
root.geometry("910x400")
root.iconbitmap("cart.ico")


def edit(ID):
    result = messagebox.askokcancel("Edit box", "Are you sure you want to edit product?\nIf you change the name of the products all the files with the previous name will no longer be available!")
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
            'oid': ID
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
    x = 1
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
    result = messagebox.askyesno("Delete", "Are you sure you want to delete item: {}?".format(str(list_box.get(ANCHOR)).split()[-1]))
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
    return


def display_report():
    return


def send_report():
    return


def start_click():
    global menu_label
    global button_1
    global button_2
    global button_3
    clear()
    products_label = Label(root, text="Compare menu", width=22)
    products_label.grid(row=0, column=0)
    button_1 = Button(root, text="Start compare", width=21, pady=10, command=start_compare)
    button_1.grid(row=1, column=0)
    button_2 = Button(root, text="Display report", width=21, pady=10, command=display_report)
    button_2.grid(row=2, column=0)
    button_3 = Button(root, text="Send report", width=21, pady=10, command=send_report)
    button_3.grid(row=3, column=0)
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

show()
root.mainloop()
