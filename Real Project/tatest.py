class User:
    def init(self, name, cart):
        self.name = name
        self.cart = cart

    def add_to_cart(self, Drink, quantity):
        item1 = Item(Drink, quantity)
        self.cart.recieve_item(item1)


class Cart:
    def init(self):
        self.item_list = []

    def recieve_item(self, item):
        self.item_list.append(item)

    def show_item_in_cart(self):
        for x in self.item_list:
            print("name: " + x.drink.name)
            print("quantity " + x.quantity)

class drink:
    def init(self, name, price):
        self.name = name
        self.price = price

class Item:
    def init(self, drink, quantity):
        self.drink = drink
        self.quantity = quantity

coke = drink("coke", 300)
coke_light = drink("coke_light", 400)

cart_user1 = Cart()
user1 = User("Racha", cart_user1)

user1.add_to_cart(coke, "1")
cart_user1.show_item_in_cart()