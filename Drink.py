from Product import Product

class Drink(Product):
    def __init__(self, name, list_of_price, description, size):
        Product.__init__(self, name, list_of_price, description)
        self.size = size