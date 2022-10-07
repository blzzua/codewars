# https://www.codewars.com/kata/59b11f57f322e5da45000254

def ones_complement(binary_number):
    return ''.join('0' if b=='1' else '1' for b in binary_number)

