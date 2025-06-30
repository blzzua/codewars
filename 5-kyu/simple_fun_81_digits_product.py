# https://www.codewars.com/kata/589436311a8808bf560000f9

from gmpy2 import is_prime
def digits_product(product):
    if product < 10:
        return 10 + product
    if is_prime(product):
        return -1
    res = ''
    for i in range(9, 1, -1):
        while product % i == 0:
            res = res + str(i)
            product = product // i
    if product == 1:
        return int(res[::-1])
    else:
        return -1

