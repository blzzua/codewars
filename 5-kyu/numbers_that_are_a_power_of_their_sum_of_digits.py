# https://www.codewars.com/kata/55f4e56315a375c1ed000159

def digit_sum(n):
    res = 0
    while n > 0:
        n, rem = divmod(n, 10)
        res += rem
    return res

RAINBOW = []
for n in range(2,100):
    for p in range(2,30):
        num = n ** p
        if n == digit_sum(num):
            RAINBOW.append(num)
RAINBOW.sort()

def power_sumDigTerm(n):
    return RAINBOW[n-1]
