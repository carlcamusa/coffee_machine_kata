from coffee_machine.customer_order import CustomerOrder


class OrderLogic:
    def __init__(self, order: CustomerOrder):
        self.order = order

    def command_for_order(self):
        return f"{self.order.command()}::"
