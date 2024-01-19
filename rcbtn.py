#Radio and check button - python

import tkinter as tk
from tkinter import *
root=tk.Tk()
root.title("my Form")
root.geometry("400x200")
l1=Label(root,text="Radio and Checkbutton python",font="sans 16 bold",bg="green",fg="yellow").pack(fill="both")

#radiobutton - single selection
v=IntVar()
r1=Radiobutton(root,variable=v,value=1,text="Male").pack()
r2=Radiobutton(root,variable=v,value=2,text="Female").pack()

#Checkbuttons- Multiple selections
c1=Checkbutton(root,text="Music").pack()
c2=Checkbutton(root,text="Movies").pack()
c3=Checkbutton(root,text="Sports").pack()
root=mainloop()
