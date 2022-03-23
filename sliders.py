from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title(" Tkinter image viewer")
root.iconbitmap('e:/project/python/tkinterTuto/phone.png')
root.geometry("500x500")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) +"x500")
horizontal = Scale(root, from_=0, to=500, orient= HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()

# def slide():
    # my_label = Label(root, text=horizontal.get()).pack()
    # root.geometry(str(horizontal.get()) +"x500")


my_button = Button(root, text="click me!", command=slide).pack()


root.mainloop()