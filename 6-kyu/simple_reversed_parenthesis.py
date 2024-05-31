# https://www.codewars.com/kata/5a3f2925b6cfd78fb0000040

def solve(st):
    if len(st) % 2 == 1:
        return -1
    res = 0
    wrongclosed = 0
    for c in st:
        wrongclosed = wrongclosed + (-1 if c == ')' else 1 if c == '(' else 0)
        if wrongclosed < 0:
            res += 1
            wrongclosed = 1
    return res + wrongclosed // 2
