from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("image viewer")
root.iconbitmap('e:/project/python/tkinterTuto/phone.png')


my_img1 = ImageTk.PhotoImage(Image.open("image/img (1).jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("image/img (2).jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("image/img (3).jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("image/img (4).jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("image/img (5).jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("image/img (6).jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("image/img (7).jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]

status = Label(root, text="Image [1] of "+ str(len(image_list)), bd=2, relief=SUNKEN, anchor= E)

my_label = Label(image=my_img1)
my_label.grid(row = 0, column = 0 , columnspan = 3)

def forward(img_num):
    global my_label, button_forward, button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[img_num-1])
    button_forward = Button(root, text=">>", command = lambda: forward(img_num+1))
    button_back = Button(root, text="<<", command= lambda: back(img_num-1))
    if img_num == 7:
        button_forward = Button(root, text=">>", state= DISABLED)
    
    my_label.grid(row = 0, column = 0 , columnspan = 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text="Image [" + str(img_num) +"] of "+ str(len(image_list)), bd=2, relief=SUNKEN, anchor= E)
    status.grid(row = 2, column=0, columnspan=3, sticky=E+W)

def back(img_num):
    global my_label, button_forward, button_back
  
    my_label.grid_forget()
    my_label = Label(image=image_list[img_num-1])
    button_forward = Button(root, text=">>", command = lambda: forward(img_num+1))
    button_back = Button(root, text="<<", command= lambda: back(img_num-1))
    if img_num == 1:
        button_back = Button(root, text="<<", state= DISABLED)
   
    my_label.grid(row = 0, column = 0 , columnspan = 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid(row = 0, column = 0 , columnspan = 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text="Image [" + str(img_num) +"] of "+ str(len(image_list)), bd=2, relief=SUNKEN, anchor= E)
    status.grid(row = 2, column=0, columnspan=3, sticky=E+W)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="exit program" ,command=root.quit)
button_forward = Button(root, text=">>", command= lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row = 2, column=0, columnspan=3, sticky=E+W)






root.mainloop()