# https://www.codewars.com/kata/58644e8ddf95f81a38001d8d

def box(n):
    return ['-'*n] + ['-' + ' '*(n - 2)  + '-']*(n - 2) + ['-'*n]

