from coffee_machine.coffee_machine import CoffeeMachine
from coffee_machine.credit_checker import CreditChecker
from coffee_machine.customer_order import CustomerOrder
from coffee_machine.drink import DrinkType
from coffee_machine.drink_maker import DrinkMaker
from coffee_machine.drink_maker_protocol import DrinkMakerProtocol
from coffee_machine.sugar_quantity import SugarQuantityType


def main():
    drink_maker_protocol = DrinkMakerProtocol()
    drink_maker = DrinkMaker()
    available_credits = 1
    credit_checker = CreditChecker(available_credits=available_credits)

    application = Application(drink_maker_protocol, drink_maker, credit_checker)

    application.run()


class Application:
    def __init__(self, drink_maker_protocol: DrinkMakerProtocol, drink_maker: DrinkMaker, credit_checker: CreditChecker):
        self.drink_maker_protocol = drink_maker_protocol
        self.drink_maker = drink_maker
        self.credit_checker = credit_checker

    def run(self):
        coffee_machine = CoffeeMachine(self.drink_maker_protocol, self.drink_maker, self.credit_checker)
        order = CustomerOrder(DrinkType.TEA, SugarQuantityType.NONE)
        coffee_machine.process_order(order)


if __name__ == "__main__":
    main()
