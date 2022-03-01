from coffee_machine.drink import DrinkType

DEFAULT_BEVERAGE_COST = {
    DrinkType.TEA: 0.4,
    DrinkType.COFFEE: 0.6,
    DrinkType.CHOCOLATE:  0.5
}

class CreditChecker:

    def __init__(self, beverage_cost: dict = DEFAULT_BEVERAGE_COST, available_credits=0):
        self.beverage_cost = beverage_cost
        self.available_credits = available_credits

    def enough_credits_available_for(self, drink_type: DrinkType):
        return self.available_credits >= self.beverage_cost[drink_type]

    def pending_amount_to(self, drink_type: DrinkType):
        if self.available_credits < self.beverage_cost[drink_type]:
            return self.beverage_cost[drink_type] - self.available_credits
        else:
            return 0
