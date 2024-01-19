# GUI program using Place()-Python

from tkinter import *
win=Tk()
win.title("Place Method")
win.geometry("820x350")
win.configure(bg="white")

Label(win,text="Welcome to MIT India \n" " you are browsing the best resource for Online Education.",font=("Vivaldi 28 italic"),fg="blue").place(x=100,y=100)
Button(win,font="tahoma 12 bold",bg="orange",text="Exit Application",command=win.destroy).place(x=650,y=220)
win.mainloop()      
