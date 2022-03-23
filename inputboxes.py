
from tkinter import *

root = Tk()

e = Entry(root, width = 50, bg='blue', fg='white', borderwidth = 5)
e.pack()
e.insert(0, "Enter your name:")
def myclick():
    hello= "hello" + e.get()
    mylabel = Label(root, text=hello)
    mylabel.pack()

mybutton = Button(root, text="Enter your name",padx = 50, pady = 20, command= myclick, fg='blue', bg='#000000')
mybutton.pack()



root.mainloop()
