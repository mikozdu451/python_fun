from tkinter import *

root = Tk()
root.title("Checkboxes")
root.geometry("400x400")

def change():
    myLabel = Label(root, text=var.get())
    myLabel.grid(row=0, column=1)


def show():
    myLabel2 = Label(root, text=clicked.get())
    myLabel2.grid(row=2, column=1)
var = StringVar()
c = Checkbutton(root, text="Option 1", variable=var, onvalue="OK", offvalue="NO")
c.deselect()
c.grid(row=0, column=0)
myButton = Button(root, text="Show answear", command=change)
myButton.grid(row=1, column=0)

dates = ["Monday", "Tuesday", "Thursday", "Wednesday", "Friday"]
clicked = StringVar()
clicked.set("Choose your value")
drop = OptionMenu(root, clicked, *dates)
drop.grid(row=2, column=0)
myButton = Button(root, text="Show answear", command=show)
myButton.grid(row=3, column=0)



root.mainloop()

