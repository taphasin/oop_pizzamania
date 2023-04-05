from Cataloug import Cataloug
from Item import Item
from NormalPizza import NormalPizza
from Cart import Cart
from User import User




pereroni = NormalPizza("Perperon", 300)
hawaian = NormalPizza("hawaian", 400)
classic_cheese = NormalPizza("classic_cheese", 285)
seafood_deluxe = NormalPizza("Seafood_deluxe", 430)



pizza_cataloug = Cataloug()
pizza_cataloug.add_item_to_list(pereroni)
pizza_cataloug.add_item_to_list(hawaian)
pizza_cataloug.add_item_to_list(classic_cheese)
pizza_cataloug.add_item_to_list(seafood_deluxe)



cart_user1 = Cart()
user1 = User("Racha", cart_user1)







if __name__ == "__main__":


    pizza_cataloug.show_item_list()




    










