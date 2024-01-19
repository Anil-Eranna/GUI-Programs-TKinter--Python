# messagebox using GUI-Phyton

from tkinter import messagebox
import tkinter as tk
root=tk.Tk()
root.title("MessageBox")
root.geometry("500x200")

lb=tk.Label(root,text="Messagebox demo",fg="white",font="sans 14").grid(row=0,column=0,columnspan=6)

def info():
    messagebox.showinfo("Info","Thank You")
b1=tk.Button(root,text="Information",bg="skyblue",command=info).grid(row=1,column=0,padx=10,pady=10)

def error():
    messagebox.showerror("Error","oh its error!")
b2=tk.Button(root,text="Error",bg="red",command=error).grid(row=1,column=1,padx=10,pady=10)    

def warn():
    messagebox.showwarning("Warning","Hello its Warning!")
b3=tk.Button(root,text="Warning",bg="orange",command=warn).grid(row=1,column=2,padx=10,pady=10)    

def askq():
    messagebox.askquestion("What!","Are you sure?")
b4=tk.Button(root,text="Are you sure?",bg="magenta",command=askq).grid(row=1,column=3,padx=10,pady=10)    

def okcan():
    messagebox.askokcancel("askokcancel","want to continue?")
b5=tk.Button(root,text="want?",bg="lightgreen",command=okcan).grid(row=1,column=4,padx=10,pady=10)    

def askyes():
    messagebox.askyesno("askyesno","Find the value?")
b6=tk.Button(root,text="YesNo",bg="skyblue",command=askyes).grid(row=1,column=5,padx=10,pady=10)

def retry():
    messagebox.askretrycancel("askretrycancel","Try again?")
b7=tk.Button(root,text="Re-try",bg="green",command=retry).grid(row=1,column=6,padx=10,pady=10)

root.mainloop()
