# https://www.codewars.com/kata/569924899aa8541eb200003f

from string import ascii_uppercase 
def quicksum(packet):
    MM = {c: i for i,c in enumerate(' ' + ascii_uppercase ) }
    return max(sum(i * MM.get(c, -999) for i, c in enumerate(packet,1)),0)

