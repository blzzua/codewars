# https://www.codewars.com/kata/56efab15740d301ab40002ee

from math import gcd
def gcdi(a,b):
    return gcd(abs(a),abs(b))

def lcmu(a, b):
    return abs(a*b)//gcd(a,b)

def som(a, b):
    return a+b

def maxi(a, b):
    return max((a,b))

def mini(a, b):
    return min((a,b))

def oper_array(fct, arr, init):
    cur = fct(arr[0], init)
    res = [cur,]
    for item in arr[1:]:
        cur = fct(cur, item)
        res.append(cur)
    return res

