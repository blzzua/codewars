# https://www.codewars.com/kata/55b350026cc02ac1a7000032

def whitespace_number(n):
    res = bin(abs(n))[2:].replace('0',' ').replace('1','\t')
    if n < 0:
        res = '\t' + res
    elif n > 0:
        res = ' ' + res
    return res + '\n'
