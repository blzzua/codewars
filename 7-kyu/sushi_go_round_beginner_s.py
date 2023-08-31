# https://www.codewars.com/kata/59619e4609868dd923000041

from math import ceil 
    
def total_bill(s):
    return 2 * (ceil(s.count('r') * 0.8))
