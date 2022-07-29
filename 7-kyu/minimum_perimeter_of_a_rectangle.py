# https://www.codewars.com/kata/5826f54cc60c7e5266000baf

import math
def divisorGenerator(n):
    # https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor

def minimum_perimeter(area):
    return min(2*(area//a+a) for a in divisorGenerator(area))



# clever
def minimum_perimeter(area):
    return next(2*(x +area//x) for x in range(int(area**0.5),0,-1) if area%x==0)
