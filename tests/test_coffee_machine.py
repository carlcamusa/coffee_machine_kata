from random import randint

from doublex import Spy, assert_that, called, Stub, ANY_ARG, Mimic

from coffee_machine.coffee_machine import CoffeeMachine
from coffee_machine.credit_checker import CreditChecker
from coffee_machine.customer_order import CustomerOrderFactory, DrinkType, SugarQuantityType
from coffee_machine.drink_maker import DrinkMaker


def test_generates_a_command_for_a_tea_order():
    drink_maker_fake = None
    credit_checker_fake = None
    coffee_machine = CoffeeMachine(drink_maker_fake, credit_checker_fake)
    an_order = CustomerOrderFactory.get(DrinkType.TEA)

    assert coffee_machine._command_for_order(an_order) == f"T::"


def test_generates_a_command_for_a_single_sugar_with_a_stick_order():
    drink_maker_fake = None
    credit_checker_fake = None
    an_order = CustomerOrderFactory.get(
        DrinkType.TEA,
        SugarQuantityType.SINGLE
    )
    coffee_machine = CoffeeMachine(drink_maker_fake, credit_checker_fake)

    assert coffee_machine._command_for_order(an_order) == f"T:1:0"


def test_generates_a_command_for_a_double_sugar_with_a_stick_order():
    drink_maker_fake = None
    credit_checker_fake = None
    an_order = CustomerOrderFactory.get(
        DrinkType.COFFEE,
        SugarQuantityType.DOUBLE
    )
    coffee_machine = CoffeeMachine(drink_maker_fake, credit_checker_fake)

    assert coffee_machine._command_for_order(an_order) == f"C:2:0"


def test_processes_an_order():
    drink_maker_spy = Mimic(Spy, DrinkMaker)
    with Stub(CreditChecker) as credit_checker_stub:
        credit_checker_stub.enough_credits_available_for(ANY_ARG).returns(True)
    coffee_machine = CoffeeMachine(drink_maker_spy, credit_checker_stub)
    an_order = CustomerOrderFactory.get(DrinkType.TEA)

    coffee_machine.process_order(an_order)

    assert_that(drink_maker_spy.set_command, called().with_args("T::"))


def test_generates_a_message_command():
    a_message = "blahblahblah"

    assert CoffeeMachine._command_for_message(a_message) == f"M:{a_message}"


def test_sends_a_message_with_the_pending_amount_when_there_is_not_enough_credit_available():
    drink_maker_spy = Mimic(Spy, DrinkMaker)
    a_pending_amount = randint(1, 10)
    with Stub(CreditChecker) as credit_checker_stub:
        credit_checker_stub.enough_credits_available_for(ANY_ARG).returns(False)
        credit_checker_stub.pending_amount_to(ANY_ARG).returns(a_pending_amount)
    coffee_machine = CoffeeMachine(drink_maker_spy, credit_checker_stub)
    an_order = CustomerOrderFactory.get(
        DrinkType.TEA,
        SugarQuantityType.NONE
    )

    coffee_machine.process_order(an_order)

    assert_that(drink_maker_spy.set_command, called().with_args(f"M:{a_pending_amount}"))


def test_integration_sends_a_message_with_the_pending_amount_when_there_is_not_enough_credit_available():
    drink_maker_spy = Mimic(Spy, DrinkMaker)
    available_credits = 0.1
    credit_checker = CreditChecker(available_credits=available_credits)
    coffee_machine = CoffeeMachine(drink_maker_spy, credit_checker)
    a_drink_type = DrinkType.TEA
    an_order = CustomerOrderFactory.get(
        a_drink_type,
        SugarQuantityType.NONE
    )
    pending_amount = credit_checker.beverage_cost[a_drink_type] - available_credits

    coffee_machine.process_order(an_order)

    assert_that(drink_maker_spy.set_command, called().with_args(f"M:{pending_amount}"))
