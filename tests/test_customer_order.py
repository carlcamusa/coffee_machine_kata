from coffee_machine.customer_order import CustomerOrderFactory, DrinkType
from coffee_machine.sugar_quantity import SugarQuantityType


def test_a_non_sugar_tea_order_drink_code():
    customer_order = CustomerOrderFactory.get(DrinkType.TEA, SugarQuantityType.NONE)
    assert customer_order.drink_code() == "T"
    assert customer_order.stick_code() == ""


def test_a_single_sugar_order_sugar_code():
    customer_order = CustomerOrderFactory.get(DrinkType.TEA, SugarQuantityType.SINGLE)
    assert customer_order.sugar_code() == "1"
    assert customer_order.stick_code() == "0"


