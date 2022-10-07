# https://www.codewars.com/kata/56598d8076ee7a0759000087

def calculate_tip(amount, rating):
    d = {
        "terrible":  0,
        "poor":  0.05,
        "good":  0.10,
        "great":  0.15,
        "excellent": 0.20,
    }
    r = rating.lower()
    if r in d:
        return int(0.99+amount * d[r])
    else:
        return 'Rating not recognised'

