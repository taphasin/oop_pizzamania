from tkinter import *
import requests
from tkinter import messagebox

API_ENDPOINT1 = "http://127.0.0.1:8000/getbill"


def on_click1():
    print("on click1")
    response = requests.post(API_ENDPOINT1, json = {"data":1} )
    messagebox.showinfo("your bill", response.json()['showbill'])

    # messagebox.showinfo('Message', pizza_message)
    
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('showitem')


button = Button(tkWindow,
	text = 'PROCEED TO CHECK OUT',
	command = on_click1)
button.pack()  

tkWindow.mainloop()
    