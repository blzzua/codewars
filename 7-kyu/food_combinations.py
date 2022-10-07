# https://www.codewars.com/kata/565f448e6e0190b0a40000cc

def actually_really_good(foods):
    l = len(foods)
    if l == 0:
        return f'You know what\'s actually really good? Nothing!'
    else:
        more = foods[0 if l == 1 else 1].lower()
        good = foods[0].capitalize()
        return f'You know what\'s actually really good? {good} and more {more}.'

