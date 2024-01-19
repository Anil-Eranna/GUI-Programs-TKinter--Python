import tkinter as tk
from tkinter import messagebox
import sys
import os

def check_login():
    entered_username=username_entry.get()
    entered_password=password_entry.get()

    if entered_username=="admin" and entered_password=="123":
        login_window.destroy()
        open_main_window()

    else:
        messagebox.showerror("Login Failed","Invalid username or password")

def open_main_window():
    main_window=tk.Tk()
    main_window.title("Main window")
    main_window.geometry("500x500+600+300")

    #add widgets or content to the main window

    label=tk.Label(main_window,text="Welcome to the window-dashboard!",font="sans 18 bold",fg="green",bg="yellow")
    label.pack(padx=20,pady=20)
    b1=tk.Button(main_window,text="Close Application",font="sans 14 bold",bg="red",fg="white",command=main_window.destroy).pack()
    
    def guif():
        import GUIform as g
    
    def mgui():
        import menugui as m

    b2=tk.Button(main_window,text="GUI Form",font="tahoma 14 bold ",bg="blue",fg="yellow",command=guif).pack(pady=20)
    b3=tk.Button(main_window,text="mene GUI",font="sans 14 bold",bg="white",fg="green",command=mgui).pack(pady=40)
    
    # Start the tkinter event loop for the main window
    main_window.mainloop()

# Create the login window
login_window=tk.Tk()
login_window.title("Login")
login_window.geometry("300x300+300+100")

label=tk.Label(login_window,text="Login here",font="sans 18 bold",bg="green",fg="yellow").pack(fill="both")

# add widgets to the login window

username_label=tk.Label(login_window,text="Username:")
username_label.pack(pady=10)

username_entry=tk.Entry(login_window)
username_entry.pack(pady=10)

password_label=tk.Label(login_window,text="Password:")
password_label.pack(pady=10)

password_entry=tk.Entry(login_window,show="*")
password_entry.pack(pady=10)

login_button=tk.Button(login_window,text="Login",command=check_login)
login_button.pack(pady=20)

#start the Tkinter event loop for the login window
login_window.mainloop()
