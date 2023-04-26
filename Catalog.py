class Catalog:
    def __init__(self):
        self.list = []
    
    def add_item_to_list(self, item):
        self.list.append(item)

    def show_item_list(self):                                              # show only NAME,  PRIECE[0]
        print("########################################################################")
        for i in self.list:
            print("name: "+ i.name, "      price: " + str(i.list_of_price[0]))
        print("########################################################################")
        