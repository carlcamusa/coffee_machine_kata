from coffee_machine.credit_checker import CreditChecker
from coffee_machine.customer_order import CustomerOrder
from coffee_machine.drink_maker import DrinkMaker


class CoffeeMachine:
    def __init__(self, drink_maker: DrinkMaker, credit_checker: CreditChecker):
        self.drink_maker = drink_maker
        self.credit_checker = credit_checker

    def process_order(self, order: CustomerOrder) -> None:
        if self.credit_checker.enough_credits_available_for(order.drink_type()):
            command = self.command_for_order(order)
        else:
            pending_credits = self.credit_checker.pending_amount_to(order.drink_type())
            command = self.command_for_message(pending_credits)

        self.drink_maker.set_command(command)

    def command_for_order(self, order: CustomerOrder):
        return f"{order.drink_code()}:{order.sugar_code()}:{order.stick_code()}"

    @staticmethod
    def command_for_message(message: str):
        return f'M:{message}'
