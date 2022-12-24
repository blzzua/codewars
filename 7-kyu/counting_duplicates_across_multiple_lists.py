# https://www.codewars.com/kata/6113c2dc3069b1001b8fdd05

def count_duplicates(name,age,height):
    return len(name) - len({(n, a, h) for n, a, h in zip(name, age, height)})
