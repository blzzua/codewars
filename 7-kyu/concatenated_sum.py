# https://www.codewars.com/kata/59a1ec603203e862bb00004f

''' MATH ONLY SOLUTION WITHOUT STRING CONVERSION '''
def check_concatenated_sum(a, k):
    print(a,k)
    orig_a = a
    sign = 1 if a > 0 else -1
    a *= sign
    arr = []
    while a > 0:
        a , rest = divmod(a, 10)
        arr.append( sum(rest * (10**i) for i in range(k)) )
    return sign * sum(arr) == orig_a
