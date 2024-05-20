# https://www.codewars.com/kata/6545283611df271da7f8418c

def three_powers(n):
    if n > 2:
        return n.bit_count() <=3
    else:
        return n.bit_count() == 3

