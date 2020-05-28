from tkinter import *


def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return


def clear():
    e.delete(0, END)


def div():
    global firstNumber
    firstNumber = float(e.get())
    global operation
    operation = "div"
    e.delete(0, END)


def mult():
    global firstNumber
    firstNumber = float(e.get())
    global operation
    operation = "mult"
    e.delete(0, END)


def sub():
    global firstNumber
    firstNumber = float(e.get())
    global operation
    operation = "sub"
    e.delete(0, END)


def add():
    global firstNumber
    firstNumber = float(e.get())
    e.delete(0, END)
    global operation
    operation = "add"


def equal():
    global seccondNumber

    try: seccondNumber = int(e.get())
    except ValueError:
        seccondNumber = 0

    e.delete(0, END)
    global answear
    if operation == "add":
        answear = firstNumber + seccondNumber
    elif operation == "sub":
        answear = firstNumber - seccondNumber
    elif operation == "mult":
        answear = firstNumber * seccondNumber
    elif operation == "div":
        try:
            answear = firstNumber / seccondNumber
        except ZeroDivisionError:
            answear = "ERROR"
    else:
        answear = 0

    if answear - int(answear) == 0:
        answear = int(answear)

    e.insert(0, answear)


root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=40, borderwidth=5, justify="right")
e.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0))
button_plus = Button(root, text="+", padx=39, pady=20, command=add)
button_equal = Button(root, text="=", padx=181, pady=20, command=equal)
button_clear = Button(root, text="C", padx=86, pady=20, command=clear)
button_div = Button(root, text="%", padx=38, pady=20, command=div)
button_mult = Button(root, text="x", padx=40, pady=20, command=mult)
button_sub = Button(root, text="-", padx=40, pady=20, command=sub)
#but the buttons

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_mult.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_plus.grid(row=4, column=3)
button_equal.grid(row=5, column=0, columnspan=4)

root.mainloop()
