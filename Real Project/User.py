class User:    
    def __init__(self, name, cart):
        self.__name = name
        self.__cart = cart

    def add_to_cart(self, pizza, chrust, cheese):
        item1 = Item(pizza, chrust, cheese)
        self.__cart.recieve_item(item1)