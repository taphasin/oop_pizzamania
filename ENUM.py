import enum
class Type(enum.Enum):
    PIZZA = 1
    DRINK = 2
class DrinkSize(enum.Enum):
    CAN = 1
    BOTTLE = 2
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
