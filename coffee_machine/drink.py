from abc import ABC, abstractmethod
from enum import Enum


class DrinkType(Enum):
    TEA = 0
    COFFEE = 1
    CHOCOLATE = 2


class DrinkFactory:
    @staticmethod
    def get(drink_type: DrinkType):
        if drink_type == DrinkType.TEA:
            return TeaDrink(drink_type)
        elif drink_type == DrinkType.COFFEE:
            return CoffeeDrink(drink_type)
        elif drink_type == DrinkType.CHOCOLATE:
            return ChocolateDrink(drink_type)
        else:
            return None


class Drink(ABC):
    def __init__(self, type: DrinkType):
        self.type = type
    @abstractmethod
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
