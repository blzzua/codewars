# https://www.codewars.com/kata/585d7b4685151614190001fd

def get_total(costs, items, tax):
    res = sum([costs.get(i, 0) for i in items])
    return round(res * (1 + tax),2)
