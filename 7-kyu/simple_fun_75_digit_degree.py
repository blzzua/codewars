# https://www.codewars.com/kata/589422431a88082ea600002a

def digit_degree(n):
    res = 0
    while n > 9:
        n = sum(int(d) for d in str(n))
        res += 1
    return res
