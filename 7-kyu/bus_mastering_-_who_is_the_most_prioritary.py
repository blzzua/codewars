# https://www.codewars.com/kata/5a0366f12b651dbfa300000c

def arbitrate(inp, n):
    ind1 = inp.find('1')
    return ''.join(['0' if i!= ind1 else '1' for i in range(n)])
