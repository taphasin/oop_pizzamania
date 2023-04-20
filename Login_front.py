from tkinter import *
import requests
from tkinter import messagebox

API_ENDPOINT1 = "http://127.0.0.1:8000/login_check"

window = Tk()
window.title("Login page")
window.geometry('360x440')

def login():
    payload = {
        "name_p"   : name.get(),
        "pass_p"   : password.get()
    }
    response = requests.post(API_ENDPOINT1, json=payload)
    messagebox.showinfo("showinfo", response.json()['data'])

name = StringVar()
password = StringVar()

login_label = Label(window, text="Login", font=("Arial", 30))
username_label = Label(window, text="Username", font=("Arial", 16))
username_entry = Entry(window, textvariable=name ,font=("Arial", 16))
password_entry = Entry(window, textvariable=password, font=("Arial", 16))
password_label = Label(window, text="Password", font=("Arial", 16))
login_button  = Button(window, text="Login", font=("Arial", 16), command=login)


login_label.grid(row=0, column=0, columnspan=2, pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

window.mainloop()
