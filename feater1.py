import enum
class DrinkSize(enum.Enum):
    CAN = 1
    BOTTLE = 2
class Product():
    def __init__(self, name, list_of_price, description):
        self._name = name
        self._list_of_price = list_of_price
        self._description = description
    
class NormalPizza(Product):
    def __init__(self, name, list_of_price, description, spicy_level, suit_for_veget):
        Product.__init__(self, name, list_of_price, description)
        self._spicy_level = spicy_level
        self._suit_for_veget = suit_for_veget

class Drink(Product):
    def __init__(self, name, list_of_price, description, size):
        Product.__init__(self, name, list_of_price, description)
        self._size = size


pizza1 = NormalPizza("ROSA GRANDE LIL’ RONI CUPS", [390, 650], "Premium Rosa Grande cup and char pepperoni flown in from the USA. Extra zesty pepperoni flavor!", 1, 0)
pizza2 = NormalPizza("KINDNESS PEPPERONI", [285, None], "Kindness brand plant-based pepperoni made with the purpose of promoting eating habits to reduce meat consumption and help combat climate change. Vegan cheese can be added free of charge.", 1, 1)
pizza3 = NormalPizza("CLASSIC CHEESE", [285, 490], "Tomato sauce, mozzarella cheese", 0, 1)
pizza4 = NormalPizza("PEPPERONI", [385, 620], "Tomato sauce, mozzarella, classic American style pepperoni. *Pepperoni is a mix of pork and beef.*", 1, 0)
pizza5 = NormalPizza("SEAFOOD DELUXE", [430, 715],"Tomato sauce, mozzarella, prawns, NZ green mussels, calamari, garlic parsley sauce", 0, 0)
pizza6 = NormalPizza("HAM & MUSHROOM", [365, 610], "Tomato sauce, butcher's ham, cremini mushrooms, Grana Padano", 0, 0)
pizza7 = NormalPizza("HAWAIIAN", [350, 585], "Tomato sauce, mozzarella, ham, pineapples, sweet corn", 0, 0)
pizza8 = NormalPizza("SUPREME", [410, 685] , "Tomato sauce, mozzarella, American style pepperoni, white onions, cremini mushrooms, roasted green capsicum, pinched Italian sausage.", 1, 0)
pizza9 = NormalPizza("BBQ CHICKEN", [390, 655], "Tomato sauce, mozzarella, roasted capsicum, bbq chicken, sautéed red onions, cheddar cheese, bbq swirl", 1, 0)
pizza10 = NormalPizza("FOUR CHEESE", [395, 655], "Tomato sauce, mozzarella, Grana Padano, smoked scamorza, gorgonzola", 0, 1)
pizza11 = NormalPizza("MEATZILLA", [430, 715], "Tomato sauce, mozzarella, seasoned ground beef, pepperoni, ham, Italian sausage, smoked bacon", 1, 0)
pizza12 = NormalPizza("CAPRICCIOSA", [405, 675], "Tomato sauce, mozzarella, ham, artichoke hearts, cremini mushrooms, Italian sausage", 0, 0)
pizza13 = NormalPizza("PARMA HAM", [425, 690], "Tomato sauce, mozzarella, freshly sliced Parma ham", 0, 0)
pizza14 = NormalPizza("THE WHITE", [385, 650], "Extra virgin olive oil, creamy NY style ricotta, caramelized onions, Grana Padano, fresh clipped basil", 0, 1)
pizza15 = NormalPizza("RICOTTA & SPINACH", [390, 645], "Tomato sauce, extra virgin olive oil, mozzarella, baby spinach, creamy NY style ricotta, Grana Padano", 0, 1)
pizza16 = NormalPizza("SALAMI & SAUSAGE", [410, 680], "Tomato sauce, mozzarella, spicy salami, Italian Sausage", 2, 0)
pizza17 = NormalPizza("EROTICA", [450, 740], "Tomato sauce, mozzarella, spicy salami, onions, mixed capsicum, black olives, Italian sausage", 2, 0)
pizza18 = NormalPizza("BOLOGNESE", [350, 580], "Tomato sauce, bolognese sauce (pork+beef mixed), mozzarella, Grana Padano - extra sauce is free BUT not recommended. Makes the pizza too wet and sloppy. No refunds available if it slides in the box.", 1, 0)
pizza19 = NormalPizza("MUSHROOM & ARTICHOKE", [365, 605], "Tomato sauce, mozzarella, cremini mushrooms, marinated Italian artichoke hearts, Grana Padano", 0, 1)
pizza20 = NormalPizza("HEALTHY GREEK", [380, 630], "Extra virigin olive oil, mozzarella, baby spinach, Kalamata olives, red onions, roasted red peppers, feta cheese", 0, 1)

drink1 = Drink("COKE - 325 ML", [45], "It's Coke.", DrinkSize.CAN)
drink2 = Drink("COKE LIGHT - 325 ML", [45], "Coke but lighter.", DrinkSize.CAN )
drink3 = Drink("COKE ZERO NO SUGAR - 325ML", [45], "Zero no sugar.", DrinkSize.CAN)
drink4 = Drink("COKE BOTTLE - 1.25L", [80], "It's Coke!", DrinkSize.CAN)
drink5 = Drink("SINGLECUT WEIRD AND GILLY NEIPA - 473ML", [250], "6.6% ABV - Soft doughy and slightly tangy malt lies under bright citrus, round tropical fruit and mild pine resin hop aromatics that underscore the waves of flavors to come. BeerAdvocate score 94.", DrinkSize.CAN)
drink6 = Drink("SINGLECUT 18-WATT AMERICAN IPA - 473ML", [250], "5% ABV - Orange zest, pine resin, and tropical lupulin beauty that easily rivals much bigger IPAs, with a substantially full, soft malt body that compliments but doesn’t interfere with the hop attack. When you want the push, weight, and attack of a much heavier (I)IPA but need to be productive tomorrow ;). BeerAdvocate Score: 92", DrinkSize.CAN)
drink7 = Drink("SINGLECUT SOFTLY SPOKEN MAGIC SPELLS NEIPA - 473ML", [325], "8.6% ABV - Golden IIPA with a tropical / bright citrus / mild pine and smooth / soft lightly sweet malt. BeerAdvocate Score: 98. Flagship.", DrinkSize.CAN)
drink8 = Drink("NIGHT SHIFT WHIRLPOOL AMERICAN PALE ALE - 473ML", [235], "4.5% ABV - Soft and citrusy, Whirlpool is a hazy New England pale ale. Pours hazy blonde with a nose of ripe peach and grapefruit. Sips juicy, fruity, and crisp, with minimal bitterness and big clementine notes. A bright, vibrant beer that’s wonderfully drinkable and remarkably refreshing. BeerAdvocate Score: 92", DrinkSize.CAN)
drink9 = Drink("NIGHT SHIFT SANTILLI AMERICAN IPA - 473ML", [250], "6% ABV - Santilli is our flagship American IPA, named after the brewery’s street address in Everett, MA. The beer pours bright gold with a nose of grapefruit zest and pine needles. Begins with big citrus flavors and a light, malty sweetness. Finishes clean, pleasantly bitter, and crisp. A boldly flavored, beautifully balanced, smooth-sipping IPA for every occasion. BeerAdvocate Score: 92.", DrinkSize.CAN)
drink10 = Drink("NIGHT SHIFT THE 87 NEIPA - 473ML", [300], "8% ABV - The 87 is a juicy, tropical New England DIPA. Pours hazy with a glowing shade of orange. A simple, clean malt bill allows the hops to shine. Aromas of sweet orange and guava lead into a stone fruit burst of candied peach and nectarine. Soft, pillowy mouthfeel. Very drinkable for 8% ABV. BeerAdvocate Score: 93", DrinkSize.CAN)
drink11 = Drink("KNEE DEEP DEEP HAZE IPA - 355ML", [200], "6.5% ABV - Cloudy, juicy, soft and super easy to drink.", DrinkSize.CAN)
drink12 = Drink("KNEE DEEP DEEP CLARITY WEST COAST IPA - 355ML", [200], "6.5% ABV - Everything you love about a West Coast IPA - clean, crisp, flavorful, and balanced with a hoppy bite.", DrinkSize.CAN)
drink13 = Drink("KNEE DEEP OOPSIE D'HAZY - 473ML", [290], "6.8% ABV - We forgot to filter and fine this ridiculously juicy New England-Inspired IPA! Served directly out of the fermenter for maximum flavor and aroma, you will taste flavors of juicy guava and ripe passionfruit that pair perfectly with its cracker-like malt profile. Take a sip and you will realize that this pillowy soft, velvety liquid was no accident!", DrinkSize.CAN)
drink14 = Drink("MAGNIFY VINE SHINE NEIPA - 473ML", [295], "6.5% ABV - This beer was inspired by both East and West coast IPAs. Drawing its dank piney hop character from the West, and its smooth light bitterness, along with its dry from the East, Vine Shine combines both styles to make a truly unique IPA. BeerAdvocate Score: 91", DrinkSize.CAN)
drink15 = Drink("REVISION PLAYAFICATION NEIPA - 473ML", [295], "6.5% ABV - A thirst-quenching, refreshing Northeast-style IPA born of 100% Mosaic hops. BeerAdvocate Score: 91", DrinkSize.CAN)
drink16 = Drink("REVISION SNARF SNARF - 473ML", [310], "8.0% ABV - A special dose of specialty malt adds schweet, schweet flavah while a combination of old and new school hops provide orange marmalade, grapefruit and forest aromas and character. BeerAdvocate Score: 90", DrinkSize.CAN)
drink17 = Drink("PORT BREWING MONGO IMPERIAL IPA - 473ML", [290], "8.0% ABV - Our flagship Double IPA, Mongo harnesses the flavor of Columbus, Cascade, Centennial, and Simcoe hops. Massive resinous aroma leads to citrus notes with a piney bitterness on the finish. BeerAdvocate Score: 93", DrinkSize.CAN)
drink19 = Drink("PORT BREWING HIGH TIDE AMERICAN IPA - 473ML", [265], "6.2% ABV - Nice citrusy IPA, drenched in notes of tangerine and stone fruit from the judicious amounts of Simcoe and Amarillo hops. BeerAdvocate score: 86", DrinkSize.CAN)
drink20 = Drink("REVISION PLAYAFICATION NEIPA - 473ML", [295], "6.5% ABV - A thirst-quenching, refreshing Northeast-style IPA born of 100% Mosaic hops. BeerAdvocate Score: 91", DrinkSize.CAN)








