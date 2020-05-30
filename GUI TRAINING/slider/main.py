from tkinter import *

root = Tk()
root.title("Slider")
root.geometry("400x400")
# vertical = Scale(root, from_=100, to=0)
# vertical.pack()


def getValue():
    myLabel = Label(root, text=horizontal.get()).pack()


def changeSize():
    root.geometry(str(horizontal.get())+"x400")


horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()
myButton = Button(root, text="Get value", command=changeSize).pack()
root.mainloop()
