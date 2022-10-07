# https://www.codewars.com/kata/58aed2cafab8faca1d000e20

def modified_sum(a, n):
    return sum(map(lambda x:pow(x,n), a)) - sum(a)

