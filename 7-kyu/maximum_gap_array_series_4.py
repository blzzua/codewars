# https://www.codewars.com/kata/5a7893ef0025e9eb50000013

def max_gap(numbers):
    numbers.sort()
    return max((abs(a-b) for a,b in zip(numbers, numbers[1:])))

