from coffee_machine.credit_checker import CreditChecker


def test_ok_when_there_is_more_than_enough_credit():
    a_drink_cost = 0.4
    available_credit = 1
    credit_checker = CreditChecker(available_credit)

    assert credit_checker.enough_credits_available_for(a_drink_cost)


def test_ok_when_there_is_exact_credit():
    a_drink_cost = 0.4
    available_credit = 0.4
    credit_checker = CreditChecker(available_credit)

    assert credit_checker.enough_credits_available_for(a_drink_cost)


def test_not_ok_when_there_is_not_enough_credit():
    a_drink_cost = 0.4
    available_credit = 0
    credit_checker = CreditChecker(available_credit)

    assert not credit_checker.enough_credits_available_for(a_drink_cost)


def test_no_pending_amount_when_there_is_enough_credit():
    a_drink_cost = 0.6
    available_credit = 1
    credit_checker = CreditChecker(available_credit)

    assert credit_checker.pending_amount_to(a_drink_cost) == 0


def test_pending_amount_when_there_is_not_enough_credit():
    a_drink_cost = 0.6
    available_credit = 0.2
    pending_amount = a_drink_cost - available_credit
    credit_checker = CreditChecker(available_credit)

    assert credit_checker.pending_amount_to(a_drink_cost) == pending_amount

