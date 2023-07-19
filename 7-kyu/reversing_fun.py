# https://www.codewars.com/kata/566efcfbf521a3cfd2000056

# from itertools import zip_longest
def reverse_fun(n):
    # fun. but fail odd tests
    # f1, f2 = n[::2], n[1::2]
    # return ''.join(c+d for c,d in zip([a+b for a,b in zip_longest(f1[::-1],f1, fillvalue='')], [ a+b for a,b in zip_longest(f2[::-1],f2, fillvalue='')]))[:len(n)]
    res = n[:]
    for i in range(len(n)):
        res = res[:i] + res[i:][::-1]
    return res
