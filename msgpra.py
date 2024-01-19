# Message box using GUI -python

from tkinter import messagebox
import tkinter as tk
window=tk.Tk()
window.title("Messagebox")
window.geometry("400x200")

heading=tk.Label(window,text="Messagebox demo",font="tahoma 14 bold",bg="white",fg="green").grid(row=0,column=0,columnspan=6)

def info():
    messagebox.showinfo("Info","Thank you")
b1=tk.Button(window,text="Information",bg="skyblue",command=info).grid(row=1,column=0,padx=10,pady=10)

def warn():
    messagebox.showwarning("warn","it is an warning")
b2=tk.Button(window,text="Warning",bg="yellow",command=warn).grid(row=1,column=1,padx=10,pady=10)    

def errorone():
    messagebox.showerror("errorone","Its an error")
b3=tk.Button(window,text="Error button",bg="green",command=errorone).grid(row=1,column=2,padx=10,pady=10)

window.mainloop()
