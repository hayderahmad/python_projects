

class Subscription:
    def __init__(self, level, Duration_of_service):
        self.durations = {"1 month": 1, "3 Months": 3,
                          '6 Months': 6, "12 Months": 12}
        if Duration_of_service not in self.durations:
            raise Exception(
                f"this is not a valid sellection please select one of the follwoing service periods 1 month, 3 Months, 6 Months, 12 Months ")

        self.duration_of_service = Duration_of_service

        if level not in ["starter", "plus", "premium"]:
            raise Exception(
                f"this is not a valid sellection please select one of the fllowing teirs starter, plus, premium and one of the follwoing service periods 1 month, 3 Months, 6 Months, 12 Months ")

        self.sub_level = level

    def get_term(self):
        return self.durations[self.duration_of_service]

    def get_level(self):
        return self.sub_level
