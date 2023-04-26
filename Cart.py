from Item import PizzaItem, DrinkItem

class Cart:
    def __init__(self):
        self.item_list = []
        self.total_price = 0

    def recieve_item(self, item):
        self.item_list.append(item)


    def calculate_total_price(self):
        total_price = 0
        for x in self.item_list:
                total_price += x.calculate_price()
        self.total_price = total_price
        print("updated total_price!!")

    def show_total_price(self):
        print("TOTAL PRICE: {} Bath".format(self.total_price))


    def show_item_in_cart(self):
        mylist = []
        for x in self.item_list:
            
            print("--------------------------------------")
            if isinstance(x, PizzaItem) == True:
                mylist.append(str(x.pizza.name))
                print("name: " + x.pizza.name)
                print("crust: " , x.crust)
                print("cook: ", x.cook)
                print("cheese: " , x.cheese)
                print("sauce: ", x.sauce)
                print("seasoning package: ", x.seasoning_package)
                converted_quantity = "{}".format(x.quantity)
                print("quantity: " + str(x.quantity))
            elif isinstance(x, DrinkItem) == True:
                mylist.append(str(x.drink.name))
                print("name: " + x.drink.name)
                #print("size " , x.size)      
                print("quantity: " + str(x.quantity))
            self.calculate_total_price()
            self.show_total_price()
            print("--------------------------------------")
        return mylist

    # def remove_item_in_cart(self, i):
    #     count = 0
    #     for x in self.item_list:
    #         if count == (i-1):
    #             self.item_list.pop(count)
    #             print("remove item[{}] successfully".format(i))
    #         count += 1


    