# https://www.codewars.com/kata/5a946d9fba1bb5135100007c

import gmpy2
def minimum_number(numbers):
    s = sum(numbers)
    if  gmpy2.is_prime(s):
        return 0
    else: 
        return gmpy2.next_prime(s)-s


