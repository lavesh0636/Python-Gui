from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("icons")
root.iconbitmap('e:/project/python/tkinterTuto/phone.png')

button_quit = Button(root, text='Exit program', command=root.quit)
button_quit.pack()


my_img = ImageTk.PhotoImage(Image.open("img.jpg"))
my_label = Label(image=my_img)
my_label.pack()









root.mainloop()