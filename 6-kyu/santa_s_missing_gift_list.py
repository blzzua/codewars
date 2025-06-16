# https://www.codewars.com/kata/5665d30b3ea3d84a2c000025

def gifts(number):
    power = 1
    res = []
    while number > 0:
        number, r = divmod(number,2)
        if r:
            res.append(GIFTS.get(power))
        power = power * 2
    return sorted(res)
