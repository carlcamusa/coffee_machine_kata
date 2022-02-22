from doublex import Spy, assert_that, called, Stub, ANY_ARG, never

from coffee_machine.credit_checker import CreditChecker
from coffee_machine.customer_order import DrinkType, CustomerOrderFactory
from coffee_machine.order_logic import OrderLogic
from coffee_machine.sugar_quantity import SugarQuantityType
from coffee_machine.drink_maker import DrinkMaker


def test_generates_a_command_for_a_tea_order():
    an_order = CustomerOrderFactory.get(DrinkType.TEA)
    drink_maker_fake = None
    credit_checker_fake = None
    order_logic = OrderLogic(an_order, drink_maker_fake, credit_checker_fake)

    assert order_logic.command_for_order() == f"T::"


def test_generates_a_command_for_a_single_sugar_with_a_stick_order():
    an_order = CustomerOrderFactory.get(
        DrinkType.TEA,
        SugarQuantityType.SINGLE
    )
    drink_maker_fake = None
    credit_checker_fake = None
    order_logic = OrderLogic(an_order, drink_maker_fake, credit_checker_fake)

    assert order_logic.command_for_order() == f"T:1:0"


def test_generates_a_command_for_a_double_sugar_with_a_stick_order():
    an_order = CustomerOrderFactory.get(
        DrinkType.COFFEE,
        SugarQuantityType.DOUBLE
    )
    drink_maker_fake = None
    credit_checker_fake = None
    order_logic = OrderLogic(an_order, drink_maker_fake, credit_checker_fake)

    assert order_logic.command_for_order() == f"C:2:0"


def test_processes_an_order():
    an_order = CustomerOrderFactory.get(DrinkType.TEA)
    drink_maker_spy = Spy(DrinkMaker)
    with Stub(CreditChecker) as credit_checker_stub:
        credit_checker_stub.enough_credits_available_for(ANY_ARG).returns(True)
    order_logic = OrderLogic(an_order, drink_maker_spy, credit_checker_stub)

    order_logic.process_order()

    assert_that(drink_maker_spy.set_command, called().with_args("T::"))

def test_sends_no_command_when_there_is_not_enough_credit_available(a_pending_amount=None):
    an_order = CustomerOrderFactory.get(
        DrinkType.TEA,
        SugarQuantityType.NONE
    )
    drink_maker_spy = Spy(DrinkMaker)
    with Stub(CreditChecker) as credit_checker_stub:
        credit_checker_stub.enough_credits_available_for(ANY_ARG).returns(False)
    order_logic = OrderLogic(an_order, drink_maker_spy, credit_checker_stub)

    order_logic.process_order()

    assert_that(drink_maker_spy.set_command, never(called()))
