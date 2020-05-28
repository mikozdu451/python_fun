from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frame")
root.iconbitmap("biohazard.ico")

frame = LabelFrame(root, text="OK let's go", padx=5, pady=5)
frame.pack()

close = Button(frame, text="Exit", command=root.quit)
close.pack()
root.mainloop()
