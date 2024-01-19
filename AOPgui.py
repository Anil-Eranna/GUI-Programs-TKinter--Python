#AOP using GUI-Event
from tkinter import *
#Object on class Tk
window=Tk()
window.title("Welcome to GUI python")
window.geometry('350x200')

#declaring controls
lb1=Label(window,text="",bg="black",font="tahoma 14 bold")

l1=Label(window,text="Num1",font=("tahoma 14 bold"))
l2=Label(window,text="Num2",font=("tahoma 14 bold"))

tx2=Entry(window,width=10,font=("tahoma 14 bold"))
tx1=Entry(window,width=10,font=("tahoma 14 bold"))

#Placing controls, using grid
l1.grid(column=0,row=0)
l2.grid(column=0,row=1)
tx1.grid(column=1,row=0)
tx2.grid(column=1,row=1)
lb1.grid(column=0,row=3,columnspan=2,sticky="nsew")

#Normal function
def add():
    res="sum",int(tx1.get())+int(tx2.get())
    lb1.configure(text=res)
btn=Button(window,text="Add",font=("tahoma 14 bold"),command=add)
btn.grid(column=0,row=4)

def sub():
    res="sub",int(tx1.get())-int(tx2.get())
    lb1.configure(text=res)
btn2=Button(window,text="Sub",font=("tahoma 14 bold"),command=sub)
btn2.grid(column=1,row=4)

def mul():
    res="mul",int(tx1.get())*int(tx2.get())
    lb1.configure(text=res)
btn3=Button(window,text="Mul",font=("tahoma 14 bold"),command=mul)
btn3.grid(column=2,row=4)
    
window.mainloop()           
