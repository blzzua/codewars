# https://www.codewars.com/kata/591d3375e51f4a0940000052

def sum_of_threes(n):
    base3 = []
    while n != 0:
        if n % 3 == 2:
            return 'Impossible'
        base3.append(n % 3)
        n = n//3
    res = []
    for i, power in enumerate(base3):
        if power: # power == 1:
            res.append(f'3^{i}')
    return '+'.join(res[::-1])

