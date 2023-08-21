# https://www.codewars.com/kata/5cd12646cf44af0020c727dd

from math import ceil, sqrt
pi = '31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

def square_pi(digits):
    return ceil(sqrt(sum(int(c)**2 for c in pi[:digits])))
