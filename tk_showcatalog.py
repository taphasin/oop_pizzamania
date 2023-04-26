from tkinter import *
import requests
from tkinter import messagebox

API_ENDPOINT1 = "http://127.0.0.1:8000/get_show_pizza"
API_ENDPOINT2 = "http://127.0.0.1:8000/get_show_drink"


# for u in pizza_cataloug.list:
#         pizza_message.append([u.name,u.price])
# for u in drink_cataloug.list:
#         drink_message.append([u.name,u.price])


def on_click1():
    print("on click1")
    response = requests.post(API_ENDPOINT1, json = {"data":1} )
    messagebox.showinfo("pizzalist", response.json()['pizzadata'])

    # messagebox.showinfo('Message', pizza_message)
    
def on_click2():
    print("on click2")
    response = requests.post(API_ENDPOINT2, json = {"data":2} )
    messagebox.showinfo("drinklist", response.json()['drinkdata'])
    # for u in drink_cataloug.list:
    #     messagebox.showinfo('Message', drink_message)


tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('showitem')


button = Button(tkWindow,
	text = 'show pizza',
	command = on_click1)
button.pack()  

button2 = Button(tkWindow,
	text = 'show drink',
	command = on_click2)
button2.pack()  
  
tkWindow.mainloop()