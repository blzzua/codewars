# https://www.codewars.com/kata/5a4d303f880385399b000001

from math import factorial
def strong_num(number):
    return ["Not Strong !!","STRONG!!!!"][sum([factorial(int(n)) for n in str(number)]) == number]

