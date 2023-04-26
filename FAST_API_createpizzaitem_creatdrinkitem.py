from typing import Union
from fastapi import FastAPI
app = FastAPI()
from Catalog import Catalog
from Item import PizzaItem
from Item import DrinkItem
from NormalPizza import NormalPizza
from Cart import Cart
from User import User
from pizzainstance import *
from ENUM import *

pizza_catalog = Catalog()
drink_catalog = Catalog()
# pizza_cataloug.add_item_to_list(pereroni)
# pizza_cataloug.add_item_to_list(hawaian)
# pizza_cataloug.add_item_to_list(classic_cheese)
# pizza_cataloug.add_item_to_list(seafood_deluxe)
pizza_catalog.add_item_to_list(pizza1)
pizza_catalog.add_item_to_list(pizza2)
pizza_catalog.add_item_to_list(pizza3)
pizza_catalog.add_item_to_list(pizza4)
pizza_catalog.add_item_to_list(pizza5)

drink_catalog.add_item_to_list(drink1)
drink_catalog.add_item_to_list(drink2)
drink_catalog.add_item_to_list(drink3)
drink_catalog.add_item_to_list(drink4)
drink_catalog.add_item_to_list(drink5)



cart_user1 = Cart()
user1 = User("Racha", cart_user1)
pizza_catalog.show_item_list()
drink_catalog.show_item_list()



from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
    return {'data':{'WELCOME':'CUSTOMER!!'}}

# @app.get("/blog")
# def index(limit = 555, published:bool = True, sort:Optional[str] = None):
#     if published:
#         return {"data", f"{limit} published blog list sort = {sort} "}
#     else:
#         return {"data", f"{limit} blogs list sort = {sort}"}

# @app.get('/blog/unpublished')
# def unpublished():
#     return {'data':'all unpublished blogs'}

# @app.get('/blog/{id}')
# def about(id: int):
#     return {'data': id}


# @app.get('/blog/{id}/comments')
# def comment(id, limit =543):
#     return {id : limit}
#     return {'data': {'1','2'}}

class BlogReq(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post('/blog')                                      # from tutorial
def create_blog(blc_req: BlogReq):
    if blc_req.published:
        return {"data" : f"blog is created!!  title = {blc_req.title}   body = {blc_req.body}  "}
    else:
        return {"data" : f"blog is created with false published  title = {blc_req.title}   body = {blc_req.body}  "}



# class PizzaItemRequest(BaseModel):                                                                                           # for show FAST API PURE
#     pizza_name : str
#     list_of_custom : list
#     quantity : int

# @app.post('/create_pizza_item')                                                                                              # for show FAST API PURE 
# def create_pizza_item(req : PizzaItemRequest):
#     for pizza in pizza_catalog.list:                     #must use getter, setter next time
#         if (req.pizza_name == pizza.name):
#             print("correct _ name pizza")
#             create_status = user1.add_pizza_to_cart(pizza, CrustSize(int(req.list_of_custom[0])),\
#                                                     CookOption(int(req.list_of_custom[1])),\
#                                                     CheeseOption(int(req.list_of_custom[2])),\
#                                                     SauceOption(int(req.list_of_custom[3])),\
#                                                     SeasoningPacket(int(req.list_of_custom[4])),\
#                                                     req.quantity)
#     cart_user1.show_item_in_cart()
#     return {"my cart" : create_status}


@app.post('/create_pizza_item')
def create_pizza_item(data : dict) -> dict:
    pizza_name = data["pizza_name"]
    crust_value = int(data["crust_value"])
    cook_value = int(data["cook_value"])
    cheese_value = int(data["cheese_value"])
    sauce_value = int(data["sauce_value"])
    seasoning_package_value = int(data["seasoning_package_value"])
    quantity_value = data["quantity_value"]
    for pizza in pizza_catalog.list:
        if pizza_name == pizza.name:
            crete_pizza_status = user1.add_pizza_to_cart(pizza, \
                                                    CrustSize(crust_value), \
                                                    CookOption(cook_value), \
                                                    CheeseOption(cheese_value), \
                                                    SauceOption(sauce_value), \
                                                    SeasoningPacket(seasoning_package_value), \
                                                    quantity_value )
            print("Added pizza to cart  SHOW ITEM IN CART:")
            cart_user1.show_item_in_cart()
            return {"my cart status" : crete_pizza_status}
    
        


@app.post('/create_drink_item')
def create_drink_item(data : dict) -> dict:
    drink_name = data["drink_name"]
    #size_value = int(data["drink_value"])
    drink_quantity_value = data["drink_quantity_value"]
    for drink in drink_catalog.list:
        if drink_name == drink.name:
            create_drink_status = user1.add_drink_to_cart(drink, \
                                                  drink_quantity_value )
            print("Added drink to cart  SHOW ITEM IN CART:")
            cart_user1.show_item_in_cart()
            return {"my cart status" : create_drink_status}

    






