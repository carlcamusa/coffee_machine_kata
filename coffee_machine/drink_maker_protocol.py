from coffee_machine.customer_order import CustomerOrder


class DrinkMakerProtocol:
    @staticmethod
    def command_for_order(order: CustomerOrder):
        return f"{order.drink_code()}:{order.sugar_code()}:{order.stick_code()}"

    @staticmethod
    def command_for_message(message: str):
        return f'M:{message}'
