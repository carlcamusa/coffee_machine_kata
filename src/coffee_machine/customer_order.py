from coffee_machine.drink import Drink, DrinkType, DrinkFactory


class CustomerOrderFactory:
    @staticmethod
    def get(drink_type: DrinkType):
        drink = DrinkFactory.get(drink_type)

        return CustomerOrder(drink)


class CustomerOrder:
    def __init__(self, drink: Drink):
        self.drink = drink

    def drink_code(self):
        return self.drink.code()
