def is_int(number):
    if type(number) != int:
        raise Exception('you should use a number')
    return number


def less_than_one(number):
    if number < 1:
        raise Exception("Hay man please don't play tricks with me")
    return number
