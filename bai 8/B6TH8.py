print("pham viet truong MSV:235752021610101")
from tkinter import *

def NewFile():
    print("New File!")
def OpenFile():
    print("OpenFile")
def Exit():
    root.quit()
def InsText():
    print("Text")
def InsPic():
    print("Picture")
def About():
    print("This is a simple example of a menu")

root = Tk()
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

insert_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insert_menu)
insert_menu.add_command(label="Text", command=InsText)
insert_menu.add_command(label="Picture", command=InsPic)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
