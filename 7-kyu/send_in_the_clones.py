# https://www.codewars.com/kata/58ddffda929dfc2cae0000a5

def clonewars(kata_per_day):
    if kata_per_day < 1: return [1, 0]
    return [2 ** (kata_per_day-1 ), 2 ** (kata_per_day+1) - kata_per_day- 2]
