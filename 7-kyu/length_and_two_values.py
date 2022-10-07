# https://www.codewars.com/kata/62a611067274990047f431a8

def cycle(first_value, second_value):
    while True:
        yield first_value
        yield second_value
        
def alternate(n, first_value, second_value):
    gen = cycle(first_value, second_value)
    return [next(gen) for _ in range(n)]



