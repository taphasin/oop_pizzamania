class Cart:
    def __init__(self):
        self.item_list = []

    def recieve_item(self, item):
        self.item_list.append(item)

    def show_item_in_cart(self):
        for x in self.item_list:
            print("name: " + x.pizza.name)
            print("crust: " + x.crust)
            print("cheese " + x.cheese)