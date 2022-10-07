# https://www.codewars.com/kata/5840586b5225616069000001

def highest_value(a, b):
    return max((a,b), key=lambda s: sum(map(ord,s)))


