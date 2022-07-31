from coffee_machine.drink import DrinkType
from coffee_machine.sugar_quantity import SugarQuantityType


class CustomerOrder:
    def __init__(self, drink_type: DrinkType, sugar_quantity_type: SugarQuantityType = SugarQuantityType.NONE):
        self.drink_type = drink_type
        self.sugar_quantity_type = sugar_quantity_type
