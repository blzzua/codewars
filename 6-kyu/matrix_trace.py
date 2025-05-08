# https://www.codewars.com/kata/55208f16ecb433c5c90001d2

def trace(matrix):
    res = 0
    n = len(matrix)
    if len(matrix) == 0:
        return None
    for i, line in enumerate(matrix):
        if len(line) != n:
            return None
        res += line[i]
    return res
