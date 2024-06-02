# https://www.codewars.com/kata/550527b108b86f700000073f

from itertools import count
def iter_pi(epsilon):
    pi = 4
    for i in count(1):
        c = ((2 * i + 1)  * (-1)**i) 
        pi = pi + 4 / c
        if abs(3.14159265358979323846 - pi ) < epsilon:
            break
    return [i+1, round(pi, 10)]
