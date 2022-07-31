from random import randint

from doublex import Spy, Stub, ANY_ARG, Mimic
from doublex_expects import have_been_called_with
from expects import expect

from coffee_machine.coffee_machine import CoffeeMachine
from coffee_machine.credit_checker import CreditChecker
from coffee_machine.customer_order import DrinkType, SugarQuantityType, CustomerOrder
from coffee_machine.drink_maker import DrinkMaker
from coffee_machine.drink_maker_protocol import DrinkMakerProtocol


class TestCoffeeMachine:
    def test_processes_a_non_sugar_tea_order(self):
        any_order_command = "any-order-command"
        with Mimic(Stub, DrinkMakerProtocol) as drink_maker_protocol:
            drink_maker_protocol.command_for_order(ANY_ARG).returns(any_order_command)
        drink_maker_spy = Mimic(Spy, DrinkMaker)
        with Stub(CreditChecker) as credit_checker_stub:
            credit_checker_stub.enough_credits_available_for(ANY_ARG).returns(True)
        coffee_machine = CoffeeMachine(drink_maker_protocol, drink_maker_spy, credit_checker_stub)
        any_order = CustomerOrder(DrinkType.TEA)

        coffee_machine.process_order(any_order)

        expect(drink_maker_spy.set_command).to(have_been_called_with(any_order_command))

    def test_sends_a_message_with_the_pending_amount_when_there_is_not_enough_credit_available(self):
        drink_maker_protocol = DrinkMakerProtocol()
        drink_maker_spy = Mimic(Spy, DrinkMaker)
        a_pending_amount = randint(1, 10)
        with Stub(CreditChecker) as credit_checker_stub:
            credit_checker_stub.enough_credits_available_for(ANY_ARG).returns(False)
            credit_checker_stub.pending_amount_to(ANY_ARG).returns(a_pending_amount)
        coffee_machine = CoffeeMachine(drink_maker_protocol, drink_maker_spy, credit_checker_stub)
        an_order = CustomerOrder(DrinkType.TEA,SugarQuantityType.NONE)

        coffee_machine.process_order(an_order)

        expect(drink_maker_spy.set_command).to(have_been_called_with(f"M:{a_pending_amount}"))
