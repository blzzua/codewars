# https://www.codewars.com/kata/56b5ebaa26fd54188b000018

def sum_proper_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

def amicable_numbers(n1,n2):
    if sum_proper_divisors(n1) == n2 and sum_proper_divisors(n2) == n1:
        return True
    return False
