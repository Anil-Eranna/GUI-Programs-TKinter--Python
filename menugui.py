# Menu in python

from tkinter import *
import sys
import os
top=Tk()

def File():
    print("File Menu selected!")
    import GUIplace as g
    #os.system("GUIplace.py")

# Creating a top level menu
menubar=Menu(top)
menubar.add_command(label="File Menu",command=File)
menubar.add_command(label="Exit",command=top.destroy)

# Display the menu
top.config(menu=menubar)

top.mainloop()
