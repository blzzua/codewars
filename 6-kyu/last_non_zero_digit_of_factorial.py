# https://www.codewars.com/kata/5f79b90c5acfd3003364a337

def last_digit(n):
    if n < 10:
        return  [1, 1, 2, 6, 4, 2, 2, 4, 2, 8][n]

    if ( n // 10 ) % 2 == 1:
        return 4 * last_digit(n // 5) * last_digit(n % 10) % 10
    else:
        return 6 * last_digit(n // 5) * last_digit(n % 10) % 10

'''
Any number can be represented as 5*a + b
For such a number the last digit is the last digit of:
    2**(a) * a! * b!
We have a property that last digit of 2^(4k + c) is last digit of 2^c
this comes from the fact that 2^4k ~ 2^4 which has a last digit of 6
and that the last digit of 6*(multiple of 2) = last digit of multiple of 2

Reference: https://www.youtube.com/watch?v=jcx_ZNEv2o0

q = n // 5
r = n % 5
last_ = 2**(q % 4) * last_digit(q) * last_digit(r)
return last_  % 10

'''
