class CreditChecker:

    def __init__(self, available_credits=0):
        self.available_credits = available_credits

    def enough_credits_available_for(self, cost: float):
        return self.available_credits >= cost
