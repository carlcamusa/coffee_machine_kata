from enum import Enum


class DrinkType(Enum):
    TEA = 0
    COFFEE = 1
    CHOCOLATE = 2


class DrinkFactory:
    @staticmethod
    def get(drink: DrinkType):
        if drink == DrinkType.TEA:
            return TeaDrink()
        elif drink == DrinkType.COFFEE:
            return CoffeeDrink()
        elif drink == DrinkType.CHOCOLATE:
            return ChocolateDrink()
        else:
            return None

class Drink:
    def code(self):
        pass


class TeaDrink(Drink):
    def code(self):
        return "T"


class CoffeeDrink(Drink):
    def code(self):
        return "C"


class ChocolateDrink(Drink):
    def code(self):
        return "H"
