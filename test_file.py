import enum
class CrustSize(enum.Enum):
    WOOD_FIRED = 1 
    NEWYORKSTYLE = 2 
class CookOption(enum.Enum):
    NORMAL = 1
    WELDONE = 2
class CheeseOption(enum.Enum):
    NORMAL = 1
    NOCHEESE = 2
    LESSCHEESE = 3
    EXTRACHEESE = 4
    DOUBLECHEESE = 5
class SauceOption(enum.Enum):
    NORMAL = 1
    NOSAUCE = 2
    LESSSAUCE = 3
    EXTRASAUCE = 4
class SeasoningPacket(enum.Enum):
    YES = 1
    NO = 2
class DrinkSize(enum.Enum):
    CAN = 1
    BOTTLE = 2
class AccountStatus(enum.Enum):
	ACTIVE = 1
	BLOCKED = 2
	BANNED = 3
	ARCHIVED = 4
	UNKNOWN = 5
class PaymentStatus(enum.Enum):
    PENDING = 1
    CONFIRMED = 2
    CANCLED = 3

class User:
    def init(self, name, cart):
        self.name = name
        self.cart = cart


class Person:
    def __init__(self, firstname, lastname, address, log_in,  account_status):
        self._firstname = firstname
        self._lastname = lastname
        self._addressid = [address]
        self._loginid = log_in
        self._account_status = account_status
        
class Login:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

class Register:
    def __init__(self, nprefix, fname, lname ,email ,mobile ,password):
        self.nameprefix = nprefix
        self.firstname = fname
        self.lastname = lname
        self.email = email
        self.mobile = mobile
        self.password = password    
class Address:
    def __init__(self, mooban, house, roadname, soi, subsoi, district, provoince, postalcode):
        self.__mooban = mooban
        self.__house = house
        self.__roadname = roadname
        self.__soi = soi
        self.__subsoi = subsoi
        self.__district = district
        self.__provoince = provoince
        self.__postalcode = postalcode
    
class Admin(Person):    
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)
    
class Customer(Person):    
    def __init__(self, firstname, lastname, cart, order):
        Person.__init__(self, firstname, lastname)
        self.__cart = cart
        self.__order = order
  
class Item:
    def init__(self, pizza, crust, cheese):
        self.pizza = pizza
        self.crust = crust
        self.cheese = cheese

class Product():
    def __init__(self, name, picture, list_of_price, description):
        self._name = name
        self._picture = picture
        self._list_of_price = list_of_price
        self._description = description

class ProductCatalog():
    def __init__(self, catalog_name):
        self.__catalog_name = catalog_name
        self.__list_product = []


class Drink(Product):
    def __init__(self, name, picture, list_of_price, description, size):
        Product.__init__(self, name, picture, list_of_price, description)
        self._size = size

class NormalPizza(Product):
    def __init__(self, name, picture, list_of_price, description, spicy_level, suit_for_veget):
        Product.__init__(self, name, picture, list_of_price, description)
        self._spicy_level = spicy_level
        self._suit_for_veget = suit_for_veget

class HalfHalfPizza(Product):
    def __init__(self, name, picture, list_of_price, description, first_half, second_half):
        Product.__init__(self, name, picture, list_of_price, description)
        self._first_half = first_half
        self._second = second_half


class DrinkOrder(Drink):
    def __init__(self, name, picture, list_of_price, description, size, quantity):
        Drink.__init__(self, name, picture, list_of_price, description, size)
        self.__quantity = quantity

class NormalPizzaOrder(NormalPizza):
    def __init__(self, name, picture, list_of_price, description, spicy_level, suit_for_veget, crust_size,\
                 cook_option, cheese_option, sauce_option, additional_instruction, quantity):
        NormalPizza.__init__(self, name, picture, list_of_price, description, spicy_level, suit_for_veget)
        self.__crust_size = crust_size
        self.__cook_option = cook_option
        self.__cheese_option = cheese_option
        self.__sauce_option = sauce_option
        self.__additional_instruc = additional_instruction
        self.__quantity = quantity
    
class HalfHalfPizzaOrder(HalfHalfPizza):
    def __init__(self, name, picture, list_of_price, description, first_half, second_half, crust_size,\
                 cheese_option_first_half, cheese_option_second_half, cook_option, sauce_option_first_half, \
                    sauce_option_second_half, additional_instruction, quantity):
        HalfHalfPizza.__init__(self, name, picture, list_of_price, description, first_half, second_half)
        self.__crust_size = crust_size
        self.__cheese_option_firsst_half = cheese_option_first_half
        self.__cheese_option_second_half = cheese_option_second_half
        self.__cook_option = cook_option
        self.__sauce_option_fisrt_half = sauce_option_first_half
        self.__sauce_option_second_half = sauce_option_second_half
        self.__additional_instruc = additional_instruction
        self.__quantity = quantity


class ProductStock():
    def __init__(self, product_name, quantity_in_stock):
        self.product_name = product_name
        self.quantity_in_stock = quantity_in_stock

class Cart():
    def __init__(self):
        self.__list_of_items = []

class Order():
    def __init__(self, order_id, list_of_item, total, owner, payment):
        self.order_id = order_id
        self.list_of_item = list_of_item
        self.total = total
        self.owner = owner
        self.payment = payment

class Payment:
    def __init__(self, payment_date, payment_status, order_id, total):
        self._payment_date = payment_date
        self._payment_status = payment_status
        self._order_id = order_id
        self._total = total
    
class CreditCardInfomation(Payment):
    def __init__(self, order_id, total, payment_method, payment_date, payment_status, card_name,\
                  expiration_date, card_numbers, cvv):
        Payment.__init__(self, order_id, total, payment_method, payment_date, payment_status)
        self.__card_name = card_name
        self.__expiration_date = expiration_date
        self.__card_numbers = card_numbers
        self.__cvv = cvv
  
class Cash(Payment):
    def __init__(self, order_id, total, payment_method, payment_date, payment_status, cash, change):
        Payment.__init__(self, order_id, total, payment_method, payment_date, payment_status)
       













# class Human():
#     def __init__(self, name):
#         self.name = name

# class Man(Human):
#     def __init__(self, name, gender):
#         Human.__init__(self, name)
#         self.gender = gender

# class Boy(Man):
#     def __init__(self, name, gender, age):
#         Boy.__init__(self, name, gender)
#         self.age = age


# boy1 = Boy("jo", "man", 10)

# print(boy1.name)




    

    
    
    
    
    
    
  
    