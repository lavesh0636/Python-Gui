from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title(" Tkinter image viewer")
root.iconbitmap('e:/project/python/tkinterTuto/phone.png')

def open():
    global my_img
    top = Toplevel()
    top.title(" Tkinter NEw Window")
    top.iconbitmap('e:/project/python/tkinterTuto/phone.png')
    lbl= Label(top, text="Heloo world").pack()
    my_img = ImageTk.PhotoImage(Image.open("image/img (1).jpg"))
    my_label = Label(top, image=my_img).pack()
    b2= Button(top, text="open second window", command=top.destroy).pack()


b= Button(root, text="open second window", command=open).pack()


# def open():
#     top = Toplevel()
#     top.title(" Tkinter NEw Window")
#     top.iconbitmap('e:/project/python/tkinterTuto/phone.png')
#     lbl= Label(top, text="Heloo world").pack()
#     my_img = ImageTk.PhotoImage(Image.open("image/img (1).jpg"))
#     my_label = Label(top, image=my_img).pack()







root.mainloop()