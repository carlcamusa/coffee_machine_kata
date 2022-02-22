from enum import Enum


class DrinkType(Enum):
    TEA = 0
    COFFEE = 1
    CHOCOLATE = 2


class CustomerOrder:
    def __init__(self, drink: DrinkType):
        self.drink = drink

    def command(self):
        if self.drink == DrinkType.TEA:
            return "T"
        elif self.drink == DrinkType.COFFEE:
            return "C"
        elif self.drink == DrinkType.CHOCOLATE:
            return "H"
        else:
            return ""
