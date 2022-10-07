# https://www.codewars.com/kata/61123a6f2446320021db987d

def prev_mult_of_three(n):
    while n> 0 and n % 3 != 0:
        n = n//10
    if n>0:
        return n

