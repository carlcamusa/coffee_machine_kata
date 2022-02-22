from enum import Enum


class DrinkType(Enum):
    TEA = 0


class CustomerOrder:
    def __init__(self, drink: DrinkType):
        self.drink = drink

    def command(self):
        if self.drink == DrinkType.TEA:
            return "T"
        else:
            return ""
