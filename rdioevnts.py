from tkinter import *
from tkinter import messagebox

ws=Tk()
ws.title("Radio events")
ws.geometry("200x200")

def ViewSelected():
    choice=var.get()
    if choice==1:
        output="Science"

    elif choice==2:
        output="Commerce"

    elif choice==3:
        output="Arts"

    else:
        output="Invalid selection"
        
    return messagebox.showinfo("Radio events",f"You Selected {output}.")

var=IntVar()
Radiobutton(ws,text="Science",variable=var, value=1, command=ViewSelected).pack()
Radiobutton(ws,text="Commerce",variable=var, value=2,command=ViewSelected).pack()
Radiobutton(ws,text="Arts",variable=var, value=3, command=ViewSelected).pack()

ws.mainloop()            
