# https://www.codewars.com/kata/58067088c27998b119000451

fact_map = {}
fact = 1
for i in range(1, 100):
    fact *= i 
    fact_map[fact] = i

def reverse_factorial(num):
    res = fact_map.get(num)
    return f'{res}!' if res else 'None'
