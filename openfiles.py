from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title(" Tkinter image viewer")
root.iconbitmap('e:/project/python/tkinterTuto/phone.png')


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="image/", title="select a file", filetypes=(("png files", "*.png"),("jpeg files","*.jpg"), ("all files", "*.*")) )
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image= my_image).pack()

my_button = Button(root, text="open file", command=open).pack()


root.mainloop()