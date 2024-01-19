# GUI using grid ()- Python

import tkinter as tk
from tkinter import *
root=tk=Tk()
root.title("Login form")
root.geometry("400x200")
l1=Label(root,text="Login here",font="sans 16 bold").grid(column=0,row=0,columnspan=2)

user=Label(root,text="Enter user name:").grid(column=0,row=1)
e1=Entry(root).grid(column=1,row=1)

passw=Label(root,text="Enter password:").grid(column=0,row=2)
e2=Entry(root,show="*").grid(column=1,row=2)

b1=Button(root,text="Sigh In").grid(column=0,row=3)
b2=Button(root,text="Cancel").grid(column=1,row=3)

root.mainloop()
