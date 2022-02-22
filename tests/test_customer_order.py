from coffee_machine.customer_order import CustomerOrder, DrinkType


def test_a_tea_order_command():
    an_order = CustomerOrder(DrinkType.TEA)

    assert an_order.command() == "T"


def test_a_coffee_order_command():
    an_order = CustomerOrder(DrinkType.COFFEE)

    assert an_order.command() == "C"


def test_a_hot_chocolate_order_command():
    an_order = CustomerOrder(DrinkType.CHOCOLATE)

    assert an_order.command() == "H"
