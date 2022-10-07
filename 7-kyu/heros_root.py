# https://www.codewars.com/kata/55efecb8680f47654c000095

def int_rac(n, guess):
    diff = n
    res = 0
    while diff >= 1:
        res += 1
        check = (guess + n / guess)//2
        diff = abs(guess - check)
        guess = check
    return res

