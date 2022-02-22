from doublex import Spy, assert_that, called

from coffee_machine.customer_order import CustomerOrder, DrinkType, CustomerOrderFactory
from coffee_machine.order_logic import OrderLogic
from coffee_machine.sugar_quantity import SugarQuantityType
from drink_maker import DrinkMaker


def test_generates_a_command_for_a_tea_order():
    an_order = CustomerOrderFactory.get(DrinkType.TEA)

    order_logic = OrderLogic(an_order)

    assert order_logic.command_for_order() == f"T::"


def test_generates_a_command_for_a_single_sugar_with_a_stick_order():
    an_order = CustomerOrderFactory.get(
        DrinkType.TEA,
        SugarQuantityType.SINGLE
    )
    drink_maker_fake = None
    order_logic = OrderLogic(an_order, drink_maker_fake)

    assert order_logic.command_for_order() == f"T:1:0"


def test_generates_a_command_for_a_double_sugar_with_a_stick_order():
    an_order = CustomerOrderFactory.get(
        DrinkType.COFFEE,
        SugarQuantityType.DOUBLE
    )
    drink_maker_fake = None
    order_logic = OrderLogic(an_order, drink_maker_fake)

    assert order_logic.command_for_order() == f"C:2:0"


def test_processes_an_order():
    an_order = CustomerOrderFactory.get(DrinkType.TEA)
    drink_maker_spy = Spy(DrinkMaker)
    order_logic = OrderLogic(an_order, drink_maker_spy)

    order_logic.process_order()

    assert_that(drink_maker_spy.set_command, called().with_args("T::"))
