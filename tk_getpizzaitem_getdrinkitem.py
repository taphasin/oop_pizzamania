from FAST_API_createpizzaitem_creatdrinkitem import *
from tkinter import *
import requests

API_CREATE_PIZZA_ITEM = "http://127.0.0.1:8000/create_pizza_item"
API_CREATE_DRINK_ITEM = "http://127.0.0.1:8000/create_drink_item"


# Create the default window
root = Tk()
root.title("Create Pizza Item")
root.geometry('700x500')

# Create the list of options
crust_list = ["1 WOOD_FIRED", "2 NEWYORKSTYLE"]
cook_list  = ["1 NORMAL", "2 WELDONE"]
cheese_list = ["1 NORMAL", "2 NOCHEESE", "3 LESSCHEESE", "4 EXTRACHEESE", "5 DOUBLECHEESE"]
sauce_list = ["1 NORMAL", "2 NOSAUCE", "3 LESSSAUCE", "4 EXTRASAUCE"]
seasoning_package_list = ["1 YES", "2 NO"]

# Variable to keep track of the option
# selected in OptionMenu
pizza_name = StringVar(root)
pizza_crust_value = StringVar(root)
pizza_cook_value = StringVar(root)
pizza_cheese_value = StringVar(root)
pizza_sauce_value = StringVar(root)
pizza_seasoning_package_value = StringVar(root)
pizza_quantity_value = IntVar(root)

drink_name = StringVar(root)
#drink_size_value = StringVar(root)
drink_quantity_value = IntVar(root)

# Set the default value of the variable
pizza_name.set("Type Pizza Name")
pizza_crust_value.set("Select Crust&Size")
pizza_cook_value.set("Select Cook Option")
pizza_cheese_value.set("Select Cheese Option")
pizza_sauce_value.set("Select Sauce Options")
pizza_seasoning_package_value.set("Select Seasoning Package")
pizza_quantity_value.set("Type quantity")


drink_name.set("Type Drink Name")
#drink_size_value.set("Select Size")
drink_quantity_value.set("Type quantity")



# Function to print the submitted option-- testing purpose
def get_pizza_item_req():
    if  pizza_crust_value.get()[0] == 'S' or pizza_cook_value.get()[0] == 'S' or pizza_cheese_value.get()[0] == 'S' or\
        pizza_sauce_value.get()[0] == 'S' or pizza_seasoning_package_value.get()[0] == 'S':
        print("YOU MUST GIVE ALL INFOMATION")
    else:
         print("**********************************************************")
         print("Selected Pizza: {}".format(pizza_name.get()))
         print("Selected Crust&Size: {}".format(pizza_crust_value.get()))
         print("Selected Cook: {}".format(pizza_cook_value.get()))
         print("Selected Cheese: {}".format(pizza_cheese_value.get()))
         print("Selected Sauce: {}".format(pizza_sauce_value.get()))
         print("Selected Seasoning Package: {}".format(pizza_seasoning_package_value.get()))
         print("Quantity: {}".format(pizza_quantity_value.get()))
         print("**********************************************************")
         for pizza in pizza_catalog.list:
            if pizza_name.get() == pizza.name:
                payload = {
                            "pizza_name" : pizza_name.get(),
                            "crust_value" : pizza_crust_value.get()[0],
                            "cook_value" : pizza_cook_value.get()[0],
                            "cheese_value" : pizza_cheese_value.get()[0],
                            "sauce_value" : pizza_sauce_value.get()[0],
                            "seasoning_package_value" : pizza_seasoning_package_value.get()[0],
                            "quantity_value" : pizza_quantity_value.get()
                            }
                response = requests.post(API_CREATE_PIZZA_ITEM, json = payload)
                if response.ok:
                    print("Add Pizza Success")
                    return
         print("Add Pizza Failed")
         return
            
    

def get_drink_item_req():
    print("**********************************************************")
    print("Selected Drink: {}".format(drink_name.get()))
    print("Quantity: {}".format(drink_quantity_value.get()))
    print("**********************************************************")
    for drink in drink_catalog.list:
        if drink_name.get() == drink.name:
            payload = {
                        "drink_name" : drink_name.get(),
                        "drink_quantity_value" : drink_quantity_value.get()
                    }
            response = requests.post(API_CREATE_DRINK_ITEM, json = payload)
            if response.ok:
                print("Add Drink Success")
                return
    print("Add Drink Fail")
    return

    
    



# Create the optionmenu widget and passing
# the options_list and value_inside to it.
pizza_name_menu = Entry(root, textvariable=pizza_name, width=20, justify="left")
pizza_name_menu.grid(row = 1 , sticky='E')
crust_menu = OptionMenu(root, pizza_crust_value, *crust_list)
crust_menu.grid(row = 2 , sticky='E')
cook_menu = OptionMenu(root, pizza_cook_value, *cook_list)
cook_menu.grid(row = 3 , sticky='E')
cheese_menu = OptionMenu(root, pizza_cheese_value, *cheese_list)
cheese_menu.grid(row = 4 , sticky='E')
sauce_menu = OptionMenu(root, pizza_sauce_value, *sauce_list)
sauce_menu.grid(row = 5 , sticky='E')
seasoning_package_menu = OptionMenu(root, pizza_seasoning_package_value, *seasoning_package_list)
seasoning_package_menu.grid(row = 6 , sticky='E')
quantity_menu = Entry(root, textvariable=pizza_quantity_value, width=20, justify="left")
quantity_menu.grid(row = 7 , sticky='E')
# Submit button
pizza_submit_button = Button(root, text='Submit Pizza ITEM', command=get_pizza_item_req)
pizza_submit_button.grid(row = 8 , sticky='E')





drink_name_menu = Entry(root, textvariable=drink_name, width=20, justify="left")
drink_name_menu.grid(row = 13 , sticky='E')
drink_quantity_menu = Entry(root, textvariable=drink_quantity_value, width=20, justify="left")
drink_quantity_menu.grid(row = 14 , sticky='E')
# Submit button
drink_submit_button = Button(root, text="Submit Drink ITEM", command=get_drink_item_req)
drink_submit_button.grid(row = 15 , sticky='E')




root.mainloop()







