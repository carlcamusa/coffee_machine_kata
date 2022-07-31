from coffee_machine.credit_checker import CreditChecker
from coffee_machine.customer_order import CustomerOrder
from coffee_machine.drink_maker import DrinkMaker
from coffee_machine.drink_maker_protocol import DrinkMakerProtocol


class CoffeeMachine:
    def __init__(self, drink_maker_protocol: DrinkMakerProtocol, drink_maker: DrinkMaker, credit_checker: CreditChecker):
        self.drink_maker_protocol = drink_maker_protocol
        self.drink_maker = drink_maker
        self.credit_checker = credit_checker

    def process_order(self, order: CustomerOrder):
        if self.credit_checker.enough_credits_available_for(order.drink_type):
            command = self.drink_maker_protocol.command_for_order(order)
        else:
            pending_credits = self.credit_checker.pending_amount_to(order.drink_type)
            command = self.drink_maker_protocol.command_for_message(pending_credits)

        self.drink_maker.set_command(command)
