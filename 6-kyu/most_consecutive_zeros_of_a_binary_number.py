# https://www.codewars.com/kata/59decdf40863c76ae3000080

from itertools import groupby
def max_consec_zeros(s):
    binary_str = bin(int(s))[2:]
    print(binary_str)
    zeroes = [len(list(data)) for g, data in groupby(binary_str) if g == '0']
    res = max(zeroes) if zeroes else 0
    return ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty'][res]
