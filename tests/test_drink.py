from coffee_machine.drink import DrinkFactory, DrinkType


def test_tea_drink_code_and_cost():
    drink = DrinkFactory.get(DrinkType.TEA)
    assert drink.code() == "T"
    assert drink.type == DrinkType.TEA


def test_coffee_drink_code_and_cost():
    drink = DrinkFactory.get(DrinkType.COFFEE)
    assert drink.code() == "C"
    assert drink.type == DrinkType.COFFEE


def test_chocolate_drink_code_and_cost():
    drink = DrinkFactory.get(DrinkType.CHOCOLATE)
    assert drink.code() == "H"
    assert drink.type == DrinkType.CHOCOLATE
