from random import randint

from doublex import Spy, assert_that, called, Stub, ANY_ARG

from coffee_machine.credit_checker import CreditChecker
from coffee_machine.customer_order import CustomerOrderFactory, DrinkType, SugarQuantityType
from coffee_machine.drink_maker import DrinkMaker
from coffee_machine.order_logic import OrderLogic


def test_generates_a_command_for_a_tea_order():
    drink_maker_fake = None
    credit_checker_fake = None
    order_logic = OrderLogic(drink_maker_fake, credit_checker_fake)
    an_order = CustomerOrderFactory.get(DrinkType.TEA)

    assert order_logic.command_for_order(an_order) == f"T::"


def test_generates_a_command_for_a_single_sugar_with_a_stick_order():
    drink_maker_fake = None
    credit_checker_fake = None
    an_order = CustomerOrderFactory.get(
        DrinkType.TEA,
        SugarQuantityType.SINGLE
    )
    order_logic = OrderLogic(drink_maker_fake, credit_checker_fake)

    assert order_logic.command_for_order(an_order) == f"T:1:0"


def test_generates_a_command_for_a_double_sugar_with_a_stick_order():
    drink_maker_fake = None
    credit_checker_fake = None
    an_order = CustomerOrderFactory.get(
        DrinkType.COFFEE,
        SugarQuantityType.DOUBLE
    )
    order_logic = OrderLogic(drink_maker_fake, credit_checker_fake)

    assert order_logic.command_for_order(an_order) == f"C:2:0"


def test_processes_an_order():
    drink_maker_spy = Spy(DrinkMaker)
    with Stub(CreditChecker) as credit_checker_stub:
        credit_checker_stub.enough_credits_available_for(ANY_ARG).returns(True)
    order_logic = OrderLogic(drink_maker_spy, credit_checker_stub)
    an_order = CustomerOrderFactory.get(DrinkType.TEA)

    order_logic.process_order(an_order)

    assert_that(drink_maker_spy.set_command, called().with_args("T::"))


def test_generates_a_message_command():
    a_message = "blahblahblah"

    assert OrderLogic.command_for_message(a_message) == f"M:{a_message}"


def test_sends_a_message_with_the_pending_amount_when_there_is_not_enough_credit_available():
    drink_maker_spy = Spy(DrinkMaker)
    a_pending_amount = randint(1, 10)
    with Stub(CreditChecker) as credit_checker_stub:
        credit_checker_stub.enough_credits_available_for(ANY_ARG).returns(False)
        credit_checker_stub.pending_amount_to(ANY_ARG).returns(a_pending_amount)
    order_logic = OrderLogic(drink_maker_spy, credit_checker_stub)
    an_order = CustomerOrderFactory.get(
        DrinkType.TEA,
        SugarQuantityType.NONE
    )

    order_logic.process_order(an_order)

    assert_that(drink_maker_spy.set_command, called().with_args(f"M:{a_pending_amount}"))


def test_integration_sends_a_message_with_the_pending_amount_when_there_is_not_enough_credit_available():
    drink_maker_spy = Spy(DrinkMaker)
    available_credits = 0.1
    credit_checker = CreditChecker(available_credits)
    order_logic = OrderLogic(drink_maker_spy, credit_checker)
    an_order = CustomerOrderFactory.get(
        DrinkType.TEA,
        SugarQuantityType.NONE
    )
    pending_amount = an_order.cost() - available_credits

    order_logic.process_order(an_order)

    assert_that(drink_maker_spy.set_command, called().with_args(f"M:{pending_amount}"))
