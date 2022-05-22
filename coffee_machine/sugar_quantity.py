from abc import abstractmethod, ABC
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


class SugarQuantity(ABC):
    @abstractmethod
    def code(self):
        pass

    @abstractmethod
    def has_sugar(self):
        pass


class NonSugarQuantity(SugarQuantity):
    def code(self):
        return ""

    def has_sugar(self):
        return False


class SingleSugarQuantity(SugarQuantity):
    def code(self):
        return "1"

    def has_sugar(self):
        return True


class DoubleSugarQuantity(SugarQuantity):
    def code(self):
        return "2"

    def has_sugar(self):
        return True
