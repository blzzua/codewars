# https://www.codewars.com/kata/57d532d2164a67cded0001c7

def histogram(results):
    res = ''
    for i, j in zip(range(6,0,-1), results[::-1]):
        res += f'{i}|' + '#' * j + (f' {j}\n' if j else '\n') 
    return res
