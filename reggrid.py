# Registration form using grid()-Python

#Importing packges
import tkinter as tk
from tkinter import *

#creating a window
window=tk.Tk()
window.title="My Form"
window.geometry="400x200"

#writing heading
heading=Label(window,text="Registration Form",font="sans 16 bold",bg="white",fg="green").grid(column=0,row=0,columnspan=2)

#Creating labels and entry box
l1=Label(window,text="Name:").grid(column=0,row=1)
e1=Entry(window).grid(column=1,row=1)
l2=Label(window,text="Email").grid(column=0,row=2)
e2=Entry(window).grid(column=1,row=2)
l3=Label(window,text="Contact Number:").grid(column=0,row=3)
e3=Entry(window).grid(column=1,row=3)

#Radiobuttons 
v=IntVar()
l4=Label(window,text="Gender").grid(column=0,row=4)
r1=Radiobutton(window,variable=v,value=1,text="Male").grid(column=1,row=4)
r2=Radiobutton(window,variable=v,value=2,text="Female").grid(column=2,row=4)

#Checkboxes
l5=Label(window,text="Hobbies:").grid(column=0,row=5)
c1=Checkbutton(window,text="Music").grid(column=1,row=5)
c2=Checkbutton(window,text="Movies").grid(column=2,row=5)
c3=Checkbutton(window,text="Sports").grid(column=3,row=5)

#buttons
b1=Button(window,text="Submit").grid(column=0,row=6)
b2=Button(window,text="Reset").grid(column=1,row=6)

window.mainloop()
