
from tkinter import *

root = Tk()

def myclick():
    mylabel = Label(root, text="Look i clicked button!!")
    mylabel.pack()

mybutton = Button(root, text="click me!",padx = 50, pady = 20, command= myclick, fg='blue', bg='#000000')
mybutton.pack()



root.mainloop()
