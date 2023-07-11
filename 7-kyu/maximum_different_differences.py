# https://www.codewars.com/kata/63adf4596ef0071b42544b9a

import gmpy2

def max_df(a_n: int) -> int:
    return (gmpy2.isqrt(8 * a_n)-1)//2

"""
    Consider the difference array containing sequential values
    D = [1, 2, ..., n] with the length n. 
    The main array A contains the values
    [1, 1+1, 1+(1+2), 1+(1+2+3), ... 1+(1+..+n)]
    The sum 1+2+...+n = n*(n+1)/2
    So with n different differences we can easily reach 
    the value Sn = n*(n+1)/2 + 1 (1). 
    Any larger value can be reached with n different differences as well,
    one can just increase the last element in the D.
    So we need to find the largest Sn which is less or equal to a_n,
    that means the largest n such as:
    n*(n+1)/2 + 1 <= a_n, or
    n**2 + n - (2*a_n - 1) <= 0
    The parabola is increasing with the positive n's, so 
    we can find the positive solution of quadratic equation
    and round it to the floor.
    D = 1 + 4 * (2 * (a_n - 1)) # discriminant
    res = (sqrt(D) - 1) // 2
"""
