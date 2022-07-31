from expects import expect, equal

from coffee_machine.customer_order import CustomerOrder
from coffee_machine.drink import DrinkType
from coffee_machine.drink_maker_protocol import DrinkMakerProtocol
from coffee_machine.sugar_quantity import SugarQuantityType


class TestDrinkMakerProtocol:
    def test_generates_a_command_for_a_non_sugar_tea_order(self):
        order = CustomerOrder(DrinkType.TEA)
        drink_maker_protocol = DrinkMakerProtocol()

        command = drink_maker_protocol.command_for_order(order)

        expect(command).to(equal("T::"))

    def test_generates_a_command_for_a_single_sugar_with_a_stick_order(self):
        order = CustomerOrder(DrinkType.TEA, SugarQuantityType.SINGLE)
        drink_maker_protocol = DrinkMakerProtocol()

        command = drink_maker_protocol.command_for_order(order)

        expect(command).to(equal("T:1:0"))

    def test_generates_a_command_for_a_double_sugar_with_a_stick_order(self):
        order = CustomerOrder(DrinkType.TEA, SugarQuantityType.DOUBLE)
        drink_maker_protocol = DrinkMakerProtocol()

        command = drink_maker_protocol.command_for_order(order)

        expect(command).to(equal("T:2:0"))

    def test_generates_a_command_message(self):
        any_message = "any-message"
        drink_maker_protocol = DrinkMakerProtocol()

        command = drink_maker_protocol.command_for_message(any_message)

        expect(command).to(equal(f"M:{any_message}"))
