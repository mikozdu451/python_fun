from tkinter import *
from tkinter import messagebox


def clicked():
    global myLabel
    myLabel = Label(root, text=r.get())
    myLabel.pack()


def pop():
    response = messagebox.askyesno("Pop up!", "Hello!")
    if response == YES:
        answear = Label(root, text="Yes")
        answear.grid(row=1)
    else:
        answear = Label(root, text="No")
        answear.grid(row=1)


root = Tk()
root.title("Radio")
# r = IntVar()
# # r.set(2)
# Radiobutton(root, text="Option: 1", variable=r, value=1, command=clicked).pack()
# Radiobutton(root, text="Option: 2", variable=r, value=2, command=clicked).pack()
#
# myLabel = Label(root, text=r.get())
# myLabel.pack()

b1 = Button(root, text="POP", command=pop)
b1.grid(row=0, column=1)
root.mainloop()
