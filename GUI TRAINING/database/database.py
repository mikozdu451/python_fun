from tkinter import *
import sqlite3

root = Tk()
root.title("Database")
root.geometry("265x275")


def submit():
    # Database
    # create a database
    conn = sqlite3.connect("addressBook.db")
    # create cursor
    cursor = conn.cursor()
    # create table
    try:
        cursor.execute("""CREATE TABLE address(
        fName text,
        lName text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
    except sqlite3.OperationalError:
        pass

    cursor.execute("INSERT INTO address VALUES (:fName, :lName, :address, :city, :state, :zipcode)",
                   {
                       'fName': fName.get(),
                       'lName': lName.get(),
                       'address': address.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zipcode': zipcode.get()
                   })

    # commit
    conn.commit()
    # close
    conn.close()
    fName.delete(0, END)
    lName.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def show():
    # Database
    # create a database
    conn = sqlite3.connect("addressBook.db")
    # create cursor
    cursor = conn.cursor()
    x = 10
    cursor.execute("SELECT *, oid FROM address")
    records = cursor.fetchall()
    for record in records:
        holder = ""
        for item in record:
            holder += str(item)+" "
        holderLabel = Label(root, text=holder)
        x += 1
        holderLabel.grid(row=x, column=0, columnspan=2)

    conn.commit()
    # close
    conn.close()


def delete():
    # create a database
    conn = sqlite3.connect("addressBook.db")
    # create cursor
    cursor = conn.cursor()

    cursor.execute("DELETE from address WHERE oid=" + deleteBox.get())
    deleteBox.delete(0, END)

    # commit
    conn.commit()
    # close
    conn.close()



def edit():
    global fNameE
    global lNameE
    global addressE
    global cityE
    global stateE
    global zipcodeE
    global recordId
    global root2
    root2 = Tk()
    root2.title("Database")
    root2.geometry("265x275")

    # create a database
    conn = sqlite3.connect("addressBook.db")
    # create cursor
    cursor = conn.cursor()
    recordId = deleteBox.get()
    cursor.execute("SELECT *, oid FROM address WHERE oid=" + recordId)
    records = cursor.fetchall()


    fNameE = Entry(root2, width=30)
    fNameE.grid(row=0, column=1, padx=10)
    lNameE = Entry(root2, width=30)
    lNameE.grid(row=1, column=1, padx=10)
    addressE = Entry(root2, width=30)
    addressE.grid(row=2, column=1, padx=10)
    cityE = Entry(root2, width=30)
    cityE.grid(row=3, column=1, padx=10)
    stateE = Entry(root2, width=30)
    stateE.grid(row=4, column=1, padx=10)
    zipcodeE = Entry(root2, width=30)
    zipcodeE.grid(row=5, column=1, padx=10)
    fNameLabelE = Label(root2, text="First name")
    fNameLabelE.grid(row=0, column=0)
    lNameLabelE = Label(root2, text="Last name")
    lNameLabelE.grid(row=1, column=0)
    addressLabelE = Label(root2, text="Adress")
    addressLabelE.grid(row=2, column=0)
    cityLabelE = Label(root2, text="City name")
    cityLabelE.grid(row=3, column=0)
    stateLabelE = Label(root2, text="State name")
    stateLabelE.grid(row=4, column=0)
    zipcodeLabelE = Label(root2, text="Zipcode")
    zipcodeLabelE.grid(row=5, column=0)
    myButtonE = Button(root2, text="Save", command=update)
    myButtonE.grid(row=6, column=0, columnspan=2, ipadx=18)
    for item in records:
        fNameE.insert(0, item[0])
        lNameE.insert(0, item[1])
        addressE.insert(0, item[2])
        cityE.insert(0, item[3])
        stateE.insert(0, item[4])
        zipcodeE.insert(0, item[5])

    # commit
    conn.commit()
    # close
    conn.close()
# Create text boxes


def update():
    # create a database
    conn = sqlite3.connect("addressBook.db")
    # create cursor
    cursor = conn.cursor()

    cursor.execute("""UPDATE address SET
    fName = :fName,
    lName = :lName,
    address = :address,
    city = :city,
    state = :city,
    zipcode = :zipcode
    
    WHERE oid =:oid""",
                   {
                       'fName': fNameE.get(),
                       'lName': lNameE.get(),
                       'address': addressE.get(),
                       'city': cityE.get(),
                       'state': stateE.get(),
                       'zipcode': zipcodeE.get(),
                       'oid': recordId
                   }

                   )
    deleteBox.delete(0, END)

    # commit
    conn.commit()
    # close
    conn.close()
    root2.destroy()

fName = Entry(root, width=30)
fName.grid(row=0, column=1, padx=10)
lName = Entry(root, width=30)
lName.grid(row=1, column=1, padx=10)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=10)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=10)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=10)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=10)

# Create text box labels

fNameLabel = Label(root, text="First name")
fNameLabel.grid(row=0, column=0)
lNameLabel = Label(root, text="Last name")
lNameLabel.grid(row=1, column=0)
addressLabel = Label(root, text="Adress")
addressLabel.grid(row=2, column=0)
cityLabel = Label(root, text="City name")
cityLabel.grid(row=3, column=0)
stateLabel = Label(root, text="State name")
stateLabel.grid(row=4, column=0)
zipcodeLabel = Label(root, text="Zipcode")
zipcodeLabel.grid(row=5, column=0)

myButton = Button(root, text="Submit", command=submit)
myButton.grid(row=6, column=0, columnspan=2, ipadx=18)

myButton2 = Button(root, text="Show records", command=show)
myButton2.grid(row=7, column=0, columnspan=2, ipadx=2)

deleteBoxLabel = Label(root, text="ID")
deleteBoxLabel.grid(row=8, column=0)
deleteBox = Entry(root, width=30)
deleteBox.grid(row=8, column=1)
myButton3 = Button(root, text="Delete records", command=delete)
myButton3.grid(row=9, column=0, columnspan=2, padx=20)
myButton4 = Button(root, text="Edit record", command=edit)
myButton4.grid(row=10, column=0, columnspan=2, ipadx=9)

root.mainloop()
