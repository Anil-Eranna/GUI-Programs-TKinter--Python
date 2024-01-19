# combo box using GUI-python

import tkinter as tk
from tkinter import *
from tkinter import ttk #ttk=themed tool kit
root=tk.Tk()
root.title("Combobox")
root.geometry("400x200")

l1=Label(root,text="Combobox",font="sans 16 bold").pack()

lang=["Python","java","C++"]
cb=ttk.Combobox(root,values=lang).pack()

b1=Button(root,text="Exit Application",command=root.destroy).pack()

root.mainloop()
