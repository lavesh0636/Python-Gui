from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title(" Tkinter image viewer")
root.iconbitmap('e:/project/python/tkinterTuto/phone.png')
# shownfo, showwarning, showerror, askquestion, askokcancel, askyesno
# def popup():
#     # messagebox.showinfo("this is my popup", "Hello world")
#     # messagebox.showwarning("this is my popup", "Hello world")
#     messagebox.showerror("this is my popup", "Hello world")
#     messagebox.askquestion("this is my popup", "Hello world")
#     messagebox.askokcancel("this is my popup", "Hello world")
#     messagebox.askyesno("this is my popup", "Hello world")

def popup():
     response = messagebox.askyesno("this is my popup", "Hello world")
     Label(root, text=response).pack()
     if response == 1:
         Label(root, text="you clicked yes").pack()
     else:
         Label(root, text="you clicked no").pack()


Button(root, text="popup", command=popup).pack()



root.mainloop()