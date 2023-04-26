from Item import PizzaItem, DrinkItem


class User:    
    def __init__(self, name, cart):
        self.__name = name
        self.__cart = cart

    def add_pizza_to_cart(self, pizza, crust, cook, cheese, sauce, seasoning_package, quantity):
        if pizza.list_of_price[crust.value - 1] == None:
            return "PIZZA Added Fail"
        else:
            item1 = PizzaItem(pizza, crust, cook, cheese, sauce, seasoning_package, quantity)
            self.__cart.recieve_item(item1)
            return "PIZZA Added Success"
    
    def add_drink_to_cart(self, drink, quantity):
        item1 = DrinkItem(drink, quantity)
        self.__cart.recieve_item(item1)
        return "DRINK Added Success"


