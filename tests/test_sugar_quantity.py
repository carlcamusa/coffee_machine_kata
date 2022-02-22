from coffee_machine.sugar_quantity import SugarQuantityFactory, SugarQuantityType


def test_non_sugar_code():
    sugar_quantity = SugarQuantityFactory.get(SugarQuantityType.NONE)
    assert sugar_quantity.code() == ""
    assert sugar_quantity.has_sugar() == False


def test_single_sugar_code():
    sugar_quantity = SugarQuantityFactory.get(SugarQuantityType.SINGLE)
    assert sugar_quantity.code() == "1"
    assert sugar_quantity.has_sugar() == True


def test_double_sugar_code():
    sugar_quantity = SugarQuantityFactory.get(SugarQuantityType.DOUBLE)
    assert sugar_quantity.code() == "2"
    assert sugar_quantity.has_sugar() == True

