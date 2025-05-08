# https://www.codewars.com/kata/58846b46f4456a8919000025

def apple_boxes(k):
    yellow, red = 0, 0
    for m in range(1,k+1):
        if m % 2 == 1:
            yellow += m**2
        else:
            red += m**2
    return red - yellow 


# clever math solution:
# Sum of n first even numbers: 2n(n+1)(2n+1)/3
# Sum of n first odd  numbers: n(2n+1)(2n-1)/3
# q, r = divmod(k, 2)
# res = (2*q*(q+1)*(2*q+1) - (q+r)*(2*(q+r)+1)*(2*(q+r)-1))//3
