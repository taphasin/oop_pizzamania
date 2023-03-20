import enum
class ProductType(enum.Enum):
    PIZZA = 1
    DRINK = 2
class ProductStock():
    def __init__(self, product_name, quantity_in_stock):
        self.product_name = product_name
        self.quantity_in_stock = quantity_in_stock

Rosa_Grande_Lil_Roni_Cups = ProductStock(ProductType.PIZZA, "Rosa Grande Lil Roni Cups", 50)
Kindness_Pepperoni = ProductStock(ProductType.PIZZA,"Kindness Pepperoni", 50)
Classic_Cheese = ProductStock(ProductType.PIZZA,"Classic Cheese", 50)
Pepperoni = ProductStock(ProductType.PIZZA,"Pepperoni", 50)
Seafood_Deluxe = ProductStock(ProductType.PIZZA,"Seafood Deluxe", 50)
Ham_and_mushroom = ProductStock(ProductType.PIZZA,"Ham & Mushroom", 50)
Hawaiian = ProductStock(ProductType.PIZZA,"Hawaiian", 50)
Supreme = ProductStock(ProductType.PIZZA,"Supreme ", 50)
BBQ_Chicken = ProductStock(ProductType.PIZZA,"BBQ Chicken", 50)
Four_Cheese = ProductStock(ProductType.PIZZA,"Four Cheese", 50)
Meatzilla = ProductStock(ProductType.PIZZA,"Meatzilla", 50)
Capricciosa = ProductStock(ProductType.PIZZA,"Capricciosa", 50)
Parma_Ham = ProductStock(ProductType.PIZZA,"Parma Ham", 50)
The_White = ProductStock(ProductType.PIZZA,"The White", 50)
Ricotta_and_Spinach = ProductStock(ProductType.PIZZA,"Ricotta & Spinach", 50)
Genovese = ProductStock(ProductType.PIZZA,"Genovese", 50)
Salami_and_Sausage = ProductStock(ProductType.PIZZA,"Salami & Sausage", 50)
Erotica = ProductStock(ProductType.PIZZA,"Erotica", 50)
Bolognese = ProductStock(ProductType.PIZZA,"Bolognese", 50)
Mushroom_and_Artichoke = ProductStock(ProductType.PIZZA,"Mushroom & Artichoke", 50)

Coke = ProductStock(ProductType.PIZZA, "Coke" , 50)
Coke_Light = ProductStock(ProductType.PIZZA, "Coke Light" , 50)
Coke_Zero_No_Sugar = ProductStock(ProductType.PIZZA, "Coke Zero No Sugar" , 50)
Coke_Bottle = ProductStock(ProductType.PIZZA, "Coke Bottle" , 50)
sSinglecut_Weird_and_Gilly_Neipa = ProductStock(ProductType.PIZZA, "sSinglecut Weird and Gilly Neipa" , 50)
Singlecut_18_Watt_American_IPA = ProductStock(ProductType.PIZZA, "Singlecut 18 Watt American IPA" , 50)
Singlecut_Softly_Spoken_Magic_Spells_Neipa = ProductStock(ProductType.PIZZA, "Singlecut Softly Spoken Magic Spells Neipa" , 50)
Night_Shift_Whirlpool_American_Pale_Ale = ProductStock(ProductType.PIZZA, "Night Shift Whirlpool American Pale Ale" , 50)
Night_Shift_Santilli_American_IPA = ProductStock(ProductType.PIZZA, "Night Shift Santilli American IPA" , 50)
Night_Shift_Santilli_American_IPA = ProductStock(ProductType.PIZZA, "Night Shift Santilli American IPA" , 50)
Knee_Deep_Deep_Haze_IPA = ProductStock(ProductType.PIZZA, "Knee Deep Deep Haze IPA" , 50)
Knee_Deep_Deep_Clarity_West_Coast_IPA = ProductStock(ProductType.PIZZA, "Knee Deep Deep Clarity West Coast IPA" , 50)
Knee_Deep_Oopsie_D_hazy = ProductStock(ProductType.PIZZA, "Knee Deep Oopsie D'hazy" , 50)
Magnify_Vine_Shine_NEIPA = ProductStock(ProductType.PIZZA, "Magnify Vine Shine NEIPA" , 50)
Revision_Playafication_NEIPA = ProductStock(ProductType.PIZZA, "Revision Playafication NEIPA" , 50)
Revision_Snarf_Snarf = ProductStock(ProductType.PIZZA, "Revision Snarf Snarf" , 50)
Port_Brewing_Mongo_Imperial_IPA = ProductStock(ProductType.PIZZA, "Port Brewing Mongo Imperial IPA" , 50)
Port_Brewing_Wipeout_American_IPA = ProductStock(ProductType.PIZZA, "Port Brewing Wipeout American IPA" , 50)
Port_Brewing_High_Tide_American_IPA = ProductStock(ProductType.PIZZA, "Port Brewing High Tide American IPA" , 50)
The_Hop_Concept_Tropical_and_Juicy_Imperial_IPA = ProductStock(ProductType.PIZZA, "The Hop Concept Tropical and Juicy Imperial IPA" , 50)