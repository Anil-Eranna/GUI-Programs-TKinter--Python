# Student details using Grid () - GUI -> Python

import tkinter as tk
from tkinter import *

window=tk.Tk()
window.title("Student details")
window.geometry("400x200")

heading=Label(window,text="Student Details",font="sans 14 bold",bg="white",fg="black").grid(row=0,column=0,columnspan=4,sticky="nsew",padx=20,pady=20)

a=Label(window,text="Student Name :").grid(row=1,column=0)
b=Label(window,text="Student reg no :").grid(row=2,column=0)
c=Label(window,text="Mobile no :").grid(row=3,column=0)
d=Label(window,text="Address :").grid(row=4,column=0)
e=Label(window,text="Gender :").grid(row=5,column=0)
f=Label(window,text="Email id :").grid(row=6,column=0)
g=Label(window,text="Course :").grid(row=7,column=0)
h=Label(window,text="Subjects :").grid(row=8,column=0)

a1=Entry(window,width=20).grid(row=1,column=1)
b1=Entry(window,width=20).grid(row=2,column=1)
c1=Entry(window,width=20).grid(row=3,column=1)
d1=Entry(window,width=20).grid(row=4,column=1)

var=IntVar()
e1=Radiobutton(window,variable=var,value=1,text="Male").grid(row=5,column=1)
e2=Radiobutton(window,variable=var,value=2,text="Female").grid(row=5,column=2)

f1=Entry(window,width=20).grid(row=6,column=1)

var2=IntVar()
g1=Radiobutton(window,variable=var2,value=3,text="BCA").grid(row=7,column=1)
g2=Radiobutton(window,variable=var2,value=4,text="BBM").grid(row=7,column=2)
g3=Radiobutton(window,variable=var2,value=5,text="B.com").grid(row=7,column=3)

h1=Checkbutton(window,text="C").grid(row=8,column=1)
h2=Checkbutton(window,text="c++").grid(row=8,column=2)
h3=Checkbutton(window,text="Java").grid(row=8,column=3)
h4=Checkbutton(window,text="Python").grid(row=8,column=4)

btn1=Button(window,text="Submit").grid(row=9,column=0)
btn2=Button(window,text="Cancel").grid(row=9,column=1)

window.mainloop()
