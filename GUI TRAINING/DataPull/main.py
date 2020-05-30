from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
root.title("Data")


def showWay():
    global myImage
    root.filename = filedialog.askopenfilename(initialdir="images", title="Select file", filetypes=(("png files", "*png"), ("all files", "*.*")))
    myLabel = Label(root, text=root.filename)
    myLabel.grid(row=1, column=0)
    myImage = ImageTk.PhotoImage(Image.open(root.filename))
    myImageLabel = Label(root, image=myImage)
    myImageLabel.grid(row=2, column=0)


myButton = Button(root, text="Select a file", command=showWay)
myButton.grid(row=0, column=0)




root.mainloop()
