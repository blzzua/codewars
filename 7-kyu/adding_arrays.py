# https://www.codewars.com/kata/59778cb1b061e877c50000cc

def arr_adder(arr):
    return ' '.join(''.join(w) for w in zip(*arr))

