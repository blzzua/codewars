# https://www.codewars.com/kata/589aca25fef1a81a10000057

def array_operations(a, k):
    if k == 0:
        return a
    else:
        m = max(a)
        for i, x in enumerate(a): 
            a[i] = m - x
        if k % 2 == 1:
            return a
        else:
            return array_operations(a, k-1)
