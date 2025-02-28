# https://www.codewars.com/kata/58b665c891e710a3ec00003f

from collections import Counter

def merge_arrays(a, b):
    a_c = Counter(a)
    b_c = Counter(b)
    c = a_c + b_c
    res = [k for k in c if a_c[k] == b_c[k] or a_c[k] * b_c[k] == 0]
    return sorted(res)
