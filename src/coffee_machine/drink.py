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

    def cost(self):
        pass


class TeaDrink(Drink):
    def code(self):
        return "T"

    def cost(self):
        return 0.4


class CoffeeDrink(Drink):
    def code(self):
        return "C"

    def cost(self):
        return 0.6


class ChocolateDrink(Drink):
    def code(self):
        return "H"

    def cost(self):
        return 0.5
