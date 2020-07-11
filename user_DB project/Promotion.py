class Promotion:
    def __init__(self, Promotion_type):
        self.database = {"christimas": 0.05, "Memorial day": 0.05, "3 Months subsicription": 0.01,
                         "6 months subscription": 0.02, "9 months subscription": 0.03}
        if Promotion_type not in self.database:
            raise Exception(f"{Promotion_type} is not a valid promotion")
        else:
            self.percent = self.database[Promotion_type]

    def get_percent(self):
        return self.percent
