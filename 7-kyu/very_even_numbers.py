# https://www.codewars.com/kata/58c9322bedb4235468000019

def is_very_even_number(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return bool(1-n%2)

