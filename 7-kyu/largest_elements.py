# https://www.codewars.com/kata/53d32bea2f2a21f666000256

from heapq import nlargest 
def largest(n,xs):
    return nlargest(n,xs)[::-1]

