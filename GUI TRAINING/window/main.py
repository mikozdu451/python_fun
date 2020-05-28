import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os


def myClick():
    mylabelbutton = Label(root, text=e.get())
    mylabelbutton.pack()


root = Tk()
myLabel = Label(root, text="Hi!")
myLabel.pack()
e = Entry(root, width="20")
e.pack()
e.insert(0, "Enter your name: ")
# canvas = tk.Canvas(root, height=500, width=500, bg="#082b4a")
# canvas.pack()
myButton = Button(root, text="Click ME!", command=myClick)
myButton.pack()
root.mainloop()
