# https://www.codewars.com/kata/557b75579b03996942000061

def serve(food, flavour, mouths):
    if flavour == 1:
        return [food/mouths] * mouths
    first = food*(flavour-1)/(flavour**mouths - 1)
    return [first * (flavour**i) for i in range(mouths)]

