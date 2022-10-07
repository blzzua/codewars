# https://www.codewars.com/kata/544aed4c4a30184e960010f4

def divisors(integer):
    res = [i for i in range(2, integer // 2 + 1) if not integer % i]
    if res:
        return res
    else:
        return f'{integer} is prime'

