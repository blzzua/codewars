# https://www.codewars.com/kata/57aa218e72292d98d500240f

from numpy import prod
def heron(*t):
    p = sum(t)/2
    return round(prod([(p-i) for i in t]+[p])**0.5,2)
         
    

