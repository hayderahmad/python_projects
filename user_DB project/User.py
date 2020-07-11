from models import Billing
from models import Promotion
from models import Subscription


class User:
    def __init__(self, subscription_level, budget, promotion_type, term):
        self.subscription = Subscription.Subscription(subscription_level, term)
        self.billing = Billing.Billinglevel(self.subscription, promotion_type)
        self.budget = budget
