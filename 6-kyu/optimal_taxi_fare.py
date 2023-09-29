# https://www.codewars.com/kata/52f51502053125863c0009d7

def calculate_optimal_fare(d, t, v1, r, v2):
    v1 = v1 / 60
    v2 = v2 / 60
    if max(v1,v2) * t < d:
        return "Won't make it!"
    if v2 >= v1:
        res = 0
    elif v1 != v2:
        res = max(0, (d - v2 * t) / (v1 - v2) * v1 * r)
    return f'{res:0.2f}'
