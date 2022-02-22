class CreditChecker:

    def __init__(self, available_credits=0):
        self.available_credits = available_credits

    def enough_credits_available_for(self, cost: float):
        return self.available_credits >= cost

    def pending_amount_to(self, cost: float):
        if self.available_credits < cost:
            return cost - self.available_credits
        else:
            return 0
