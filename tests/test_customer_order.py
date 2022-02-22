from coffee_machine.customer_order import CustomerOrder, DrinkType


def test_a_tea_order_command():
    an_order = CustomerOrder(DrinkType.TEA)

    assert an_order.command() == "T"
