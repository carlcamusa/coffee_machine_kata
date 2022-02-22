from coffee_machine.customer_order import CustomerOrderFactory, DrinkType


def test_a_tea_order_drink_code():
    customer_order = CustomerOrderFactory.get(DrinkType.TEA)
    assert customer_order.drink_code() == "T"
