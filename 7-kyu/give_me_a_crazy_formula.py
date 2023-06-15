# https://www.codewars.com/kata/5661cde807c4e28efa0000d0

def cycle(n):
    strn = str(n)
    if len(strn) % 2 == 0:
        n = int(strn[:-1])
        return n

    mid_ind = len(strn)//2
    str_l = [int(c) for c in str(n)]
    if str_l[mid_ind] % 2 == 1:
        str_l[mid_ind] = - str_l[mid_ind]
    else:
        if str_l[-1] % 2 == 0:
            str_l[-1] = -str_l[-1]
        else:
            str_l[0] = str_l[0] ** 2
    return abs(sum(str_l))
    
def crazy_formula(n):
    while n > 9:
        n = cycle(n)
    return n
