# https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5

def reverse_number(n):
    # reverse string too easy
    # math:
    sign = -1 if n < 0 else 1 
    n = abs(n)
    res = []
    while n > 0:
        n, r = divmod(n, 10)
        res.append(r)
    return sign * sum(10 ** i * d for i,d in enumerate(res[::-1]))

