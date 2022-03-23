from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("image viewer")
root.iconbitmap('e:/project/python/tkinterTuto/phone.png')

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=100, pady=100)

b = Button(frame, text="Click Heree!")
b.grid(row = 0, column=0) 

b1 = Button(frame, text="Click Heree!")
b1.grid(row = 1, column=1) 









root.mainloop()