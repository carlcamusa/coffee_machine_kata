from enum import Enum

class SugarQuantityType(Enum):
    NONE = 0
    SINGLE = 1
    DOUBLE = 2


class SugarQuantityFactory:
    @staticmethod
    def get(quantity: SugarQuantityType):
        if quantity == SugarQuantityType.NONE:
            return NonSugarQuantity()
        elif quantity == SugarQuantityType.SINGLE:
            return SingleSugarQuantity()
        elif quantity == SugarQuantityType.DOUBLE:
            return DoubleSugarQuantity()
        else:
            return None


class SugarQuantity:
    def code(self):
        pass


class NonSugarQuantity(SugarQuantity):
    def code(self):
        return ""


class SingleSugarQuantity(SugarQuantity):
    def code(self):
        return "1"


class DoubleSugarQuantity(SugarQuantity):
    def code(self):
        return "2"
