from typing import Dict

from coffee_machine.customer_order import CustomerOrder
from coffee_machine.drink import DrinkType
from coffee_machine.sugar_quantity import SugarQuantityType

DEFAULT_BEVERAGE_CODE = {
    DrinkType.TEA: "T",
    DrinkType.COFFEE: "C",
    DrinkType.CHOCOLATE: "H",
}

DEFAULT_SUGAR_QUANTITY_CODE = {
    SugarQuantityType.NONE: "",
    SugarQuantityType.SINGLE: "1",
    SugarQuantityType.DOUBLE: "2",
}


class DrinkMakerProtocol:
    beverage_code: Dict[DrinkType, str] = DEFAULT_BEVERAGE_CODE
    sugar_quantity_code: Dict[SugarQuantityType, str] = DEFAULT_SUGAR_QUANTITY_CODE

    @classmethod
    def command_for_order(cls, order : CustomerOrder):
        return f"{cls._drink_code(order)}:{cls._sugar_quantity_code(order)}:{cls._stick_code(order)}"

    @staticmethod
    def command_for_message(message: str):
        return f'M:{message}'

    @classmethod
    def _drink_code(cls, order: CustomerOrder):
        return cls.beverage_code[order.drink_type]

    @classmethod
    def _sugar_quantity_code(cls, order: CustomerOrder):
        return cls.sugar_quantity_code[order.sugar_quantity_type]

    @classmethod
    def _stick_code(cls, order: CustomerOrder):
        if order.sugar_quantity_type == SugarQuantityType.NONE:
            return ""
        else:
            return "0"

