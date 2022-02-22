from coffee_machine.drink import DrinkFactory, DrinkType


def test_tea_drink_code():
    drink = DrinkFactory.get(DrinkType.TEA)
    assert drink.code() == "T"


def test_coffee_drink_code():
    drink = DrinkFactory.get(DrinkType.COFFEE)
    assert drink.code() == "C"


def test_chocolate_drink_code():
    drink = DrinkFactory.get(DrinkType.CHOCOLATE)
    assert drink.code() == "H"
