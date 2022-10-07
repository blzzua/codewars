# https://www.codewars.com/kata/54e2213f13d73eb9de0006d2

def pair_zeros(arr):
    flag = 0
    def spin():
        nonlocal flag
        flag = 1-flag
        return flag
    return [i for i in arr if i>0 or spin() ]

