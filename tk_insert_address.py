from tkinter import *
import requests
from tkinter import messagebox

API_ENDPOINT1 = "http://127.0.0.1:8000/add_address"


def address():
    payload = {
        "address"  : input_address.get()
        }
    response = requests.post(API_ENDPOINT1, json=payload)
    messagebox.showinfo("showinfo", response.json()['data'])


tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('address')

input_address = StringVar()

Address_label    = Label(tkWindow, text="Insert Delivery Address", font=("Arial", 16))
Address_entry    = Entry(tkWindow, textvariable=input_address, font=("Arial", 16))
submit_button = Button(tkWindow, text="submit", font=("Arial", 16), command=address)
Address_label.pack()
Address_entry.pack()
submit_button.pack()


tkWindow.mainloop()
    