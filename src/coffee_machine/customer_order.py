from coffee_machine.drink import Drink, DrinkType, DrinkFactory
from coffee_machine.sugar_quantity import SugarQuantityFactory, SugarQuantityType, SugarQuantity


class CustomerOrderFactory:
    @staticmethod
    def get(drink_type: DrinkType, sugar_quantity_type: SugarQuantityType = SugarQuantityType.NONE):
        drink = DrinkFactory.get(drink_type)
        sugar_quantity = SugarQuantityFactory.get(sugar_quantity_type)

        return CustomerOrder(drink, sugar_quantity)


class CustomerOrder:
    def __init__(self, drink: Drink, sugar_quantity: SugarQuantity):
        self.drink = drink
        self.sugar_quantity = sugar_quantity

    def drink_code(self):
        return self.drink.code()

    def sugar_code(self):
        return self.sugar_quantity.code()

    def has_sugar(self):
        return self.sugar_quantity.has_sugar()

    def cost(self):
        return self.drink.cost()
