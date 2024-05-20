# https://www.codewars.com/kata/572bbd7c72a38bd878000a73

from math import gcd

class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
    
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
        
    def __add__(self, other):
        res_top = self.bottom * other.top + self.top * other.bottom
        res_bottom = self.bottom * other.bottom
        cd = gcd(res_top, res_bottom)
        self.top = res_top // cd
        self.bottom = res_bottom // cd
        return self
    
    def __repr__(self):
        return f'{self.top}/{self.bottom}'
