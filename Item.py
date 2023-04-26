class PizzaItem:
    def __init__(self, pizza, crust, cook, cheese, sauce, seasoning_package, quantity):
        self.pizza = pizza
        self.crust = crust
        self.cook = cook
        self.cheese = cheese
        self.sauce = sauce
        self.seasoning_package = seasoning_package
        self.quantity = quantity
        self.item_price = 0
    
    def calculate_price(self):              # this method is re-calc self.item price  and set value to self.item_price at the same timm
        self.item_price = self.pizza.list_of_price[self.crust.value - 1]
        if self.cheese.value == 4:
            self.item_price  += 30
        elif self.cheese.value == 5:
            self.item_price += 60
        self.item_price *= self.quantity
        return self.item_price

        
class DrinkItem:
    def __init__(self, drink, quantity):
        self.drink = drink  
        #self.size = size                        
        self.quantity = quantity
        self.item_price = 0

    def calculate_price(self):          # thsi method is re-calc self.item price  and set value to self.item_price at the same time
        total = 0
        total = self.drink.list_of_price[self.drink.size.value - 1]
        total = total * self.quantity
        self.item_price = total
        return self.item_price