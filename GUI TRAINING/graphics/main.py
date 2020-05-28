from tkinter import *
from PIL import ImageTk, Image


def forward(num):
    global label
    global button_forward
    global button_back
    global status
    label.grid_forget()
    label = Label(image=list_img[num-1])
    label.grid(row=0, column=0, columnspan=3)
    button_forward = Button(root, text=">>", command= lambda: forward(num+1))
    button_back = Button(root, text="<<", command= lambda: back(num-1))
    status = Label(root, text="Image {} of {}".format(num, len(list_img)))
    if num == len(list_img):
        button_forward = Button(root, text=">>", state=DISABLED)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3)


def back(num):
    global label
    global button_forward
    global button_back
    label.grid_forget()
    label = Label(image=list_img[num-1])
    label.grid(row=0, column=0, columnspan=3)
    button_forward = Button(root, text=">>", command= lambda: forward(num+1))
    button_back = Button(root, text="<<", command= lambda: back(num-1))
    status = Label(root, text="Image {} of {}".format(num, len(list_img)))
    if num == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3)


root = Tk()
root.title("App")
root.iconbitmap("biohazard.ico")
img1 = ImageTk.PhotoImage(Image.open("images\gorrilaz.png"))
img2 = ImageTk.PhotoImage(Image.open("images\dobranoc.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images\mikolaje.jpg"))

list_img = [img1, img2, img3]
print(len(list_img))
label = Label(image=list_img[0])
label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", command= lambda: back, state=DISABLED)
buttonQuit = Button(root, text="Close program", command=root.quit)
button_forward = Button(root, text=">>", command= lambda: forward(2))
button_back.grid(row=1, column=0)
buttonQuit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

status = Label(root, text="Image 1 of {}".format(len(list_img)))
status.grid(row=2, column=0, columnspan=3, sticky=W+E, )



root.mainloop()
