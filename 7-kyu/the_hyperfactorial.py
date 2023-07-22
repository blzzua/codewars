# https://www.codewars.com/kata/6324786fcc1a9700260a2147

from math import factorial, prod

def hyperfact(num):
    return prod(map(lambda x: x ** x,range(1,num+1))) % 1000000007
