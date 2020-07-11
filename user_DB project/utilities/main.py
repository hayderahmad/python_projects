from modules import User

hassuny = User.User("starter", 654, "3 Months subsicription", "3 Months")
print(hassuny.billing.get_Total())
