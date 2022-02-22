from coffee_machine.customer_order import CustomerOrder
from drink_maker import DrinkMaker


class OrderLogic:
    def __init__(self, order: CustomerOrder, drink_maker: DrinkMaker = None):
        self.order = order
        self.drink_maker = drink_maker

    def command_for_order(self):
        return f"{self.order.drink_code()}:{self.order.sugar_code()}:"

    def process_order(self) -> None:
        command = self.command_for_order()
        self.drink_maker.set_command(command)
