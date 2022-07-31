from coffee_machine.credit_checker import CreditChecker, DEFAULT_BEVERAGE_COST
from coffee_machine.drink import DrinkType

class TestCreditChecker:
    def test_ok_when_there_is_more_than_enough_credit(self):
        a_drink_type = DrinkType.TEA
        available_credit = DEFAULT_BEVERAGE_COST[a_drink_type] + 1
        credit_checker = CreditChecker(available_credits=available_credit)

        assert credit_checker.enough_credits_available_for(a_drink_type)


    def test_ok_when_there_is_exact_credit(self):
        a_drink_type = DrinkType.TEA
        available_credit = DEFAULT_BEVERAGE_COST[a_drink_type]
        credit_checker = CreditChecker(available_credits=available_credit)

        assert credit_checker.enough_credits_available_for(a_drink_type)


    def test_not_ok_when_there_is_not_enough_credit(self):
        a_drink_type = DrinkType.TEA
        available_credit = 0
        credit_checker = CreditChecker(available_credits=available_credit)

        assert not credit_checker.enough_credits_available_for(a_drink_type)


    def test_no_pending_amount_when_there_is_enough_credit(self):
        a_drink_type = DrinkType.TEA
        available_credit = DEFAULT_BEVERAGE_COST[a_drink_type] + 1
        credit_checker = CreditChecker(available_credits=available_credit)

        assert credit_checker.pending_amount_to(a_drink_type) == 0


    def test_pending_amount_when_there_is_not_enough_credit(self):
        a_drink_type = DrinkType.TEA
        available_credit = DEFAULT_BEVERAGE_COST[a_drink_type] - 0.2
        pending_amount = DEFAULT_BEVERAGE_COST[a_drink_type] - available_credit
        credit_checker = CreditChecker(available_credits=available_credit)

        assert credit_checker.pending_amount_to(a_drink_type) == pending_amount

