from doublex import Spy, assert_that, called

from coffee_machine.customer_order import CustomerOrder, DrinkType
from coffee_machine.order_logic import OrderLogic
from drink_maker import DrinkMaker


def test_generates_a_command_for_a_tea_order():
    an_order = CustomerOrder(DrinkType.TEA)

    order_logic = OrderLogic(an_order)

    assert order_logic.command_for_order() == f"T::"

def test_processes_an_order():
    an_order = CustomerOrder(DrinkType.TEA)
    drink_maker_spy = Spy(DrinkMaker)
    order_logic = OrderLogic(an_order, drink_maker_spy)

    order_logic.process_order()

    assert_that(drink_maker_spy.set_command, called().with_args("T::"))