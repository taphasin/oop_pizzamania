from tkinter import *
import requests
from tkinter import messagebox

API_ENDPOINT2 = "http://127.0.0.1:8000/Register"


def login():
    payload = {
        "prefix_p"  : input_prefix.get(),
        "fname_p"   : input_fname.get(),
        "lname_p"   : input_lname.get(),
        "email_p"   : input_email.get(),
        "mobile_p"  : input_mobile.get(),
        "pass_p"    : input_password.get()
        }
    response = requests.post(API_ENDPOINT2, json=payload)
    messagebox.showinfo("showinfo", response.json()['data'])


window = Tk()
window.title("Register page")
window.geometry('360x500')

input_fname    = StringVar()
input_password = StringVar()
input_prefix   = StringVar()
input_lname    = StringVar()
input_email    = StringVar()
input_mobile   = StringVar()

login_label     = Label(window, text="Register", font=("Arial", 30))

prefix_label    = Label(window, text="Prefix", font=("Arial", 16))
prefix_entry    = Entry(window, textvariable=input_prefix, font=("Arial", 16))

fname_label     = Label(window, text="Firstrname", font=("Arial", 16))
fname_entry     = Entry(window, textvariable=input_fname ,font=("Arial", 16))

lname_label     = Label(window, text="Lastname", font=("Arial", 16))
lname_entry     = Entry(window, textvariable=input_lname ,font=("Arial", 16))

email_label     = Label(window, text="email", font=("Arial", 16))
email_entry     = Entry(window, textvariable=input_email, font=("Arial", 16))

mobile_lable    = Label(window, text="mobile", font=("Arial", 16))
mobile_entry    = Entry(window, textvariable=input_mobile, font=("Arial", 16))

password_label  = Label(window, text="Password", font=("Arial", 16))
password_entry  = Entry(window, textvariable=input_password, font=("Arial", 16))

login_button    = Button(window, text="Login", font=("Arial", 16), command=login)



login_label.grid(row=0, column=0, columnspan=2, pady=40)

prefix_label.grid(row=1, column=0)
prefix_entry.grid(row=1, column=1)

fname_label.grid(row=2, column=0)
fname_entry.grid(row=2, column=1, pady=20)

lname_label.grid(row=3, column=0)
lname_entry.grid(row=3, column=1, pady=10)

email_label.grid(row=4, column=0)
email_entry.grid(row=4, column=1, pady=10)

mobile_lable.grid(row=5, column=0)
mobile_entry.grid(row=5, column=1, pady=10)

password_label.grid(row=6, column=0)
password_entry.grid(row=6, column=1, pady=10)

login_button.grid(row=7, column=0, columnspan=2, pady=30)

window.mainloop()