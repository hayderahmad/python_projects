from models import Promotion


class Billinglevel:
    def __init__(self, sub, promotion_type):
        self.promotion = Promotion.Promotion(promotion_type)
        self.sub = sub
        if sub.sub_level == "starter":
            self.__sub_price = 2.99-2.99 * self.promotion.percent
        if sub.sub_level == "plus":
            self.__sub_price = 5.99-5.99 * self.promotion.percent
        if sub.sub_level == "premium":
            self.__sub_price = 9.99-9.99 * self.promotion.percent

    def get_Total(self):
        return self.__sub_price * self.sub.get_term()
