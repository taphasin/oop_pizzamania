from Product import Product

class NormalPizza(Product):
    def __init__(self, name, list_of_price, description, spicy_level, suit_for_veget):
        Product.__init__(self, name, list_of_price, description)
        self._spicy_level = spicy_level
        self._suit_for_veget = suit_for_veget