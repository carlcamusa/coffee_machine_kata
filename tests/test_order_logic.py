from coffee_machine.customer_order import CustomerOrder, DrinkType
from coffee_machine.order_logic import OrderLogic


def test_generates_a_command_for_a_tea_order():
    an_order = CustomerOrder(DrinkType.TEA)

    order_logic = OrderLogic(an_order)

    assert order_logic.command_for_order() == f"T::"
