from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title(" Tkinter image viewer")
root.iconbitmap('e:/project/python/tkinterTuto/phone.png')

#r = IntVar()  #str var
#r.set(2)

toppeings = [
    ("peporrani", "peporrani"),
    ("onion", "onion"),
    ("mushrom", "mushrom"),
    ("chesse", "chesse")
]

pizza = StringVar()
pizza.set('peporrani')

for text, mode in toppeings:
    Radiobutton(root, text=text , variable=pizza, value=mode).pack(anchor = W)

def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()

#creating radio buttona
#Radiobutton(root, text="option 1", variable=r, value=1, command= lambda: clicked(r.get())).pack()
#Radiobutton(root, text="option 2", variable=r, value=2, command = lambda: clicked(r.get())).pack()


button = Button(root, text="click me!", command= lambda: clicked(pizza.get())).pack()

# mylabel = Label(root, text=pizza.get())
# mylabel.pack()







root.mainloop()