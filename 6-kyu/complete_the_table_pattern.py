# https://www.codewars.com/kata/5827e2efc983ca6f230000e0

def pattern(rows, columns, s):
    s = s.ljust(rows * columns)
    h1 = '---'.join('+'* (columns+1))
    res = [h1]
    for i, sub in enumerate(map(''.join, zip(*[iter(s)]*columns))):
        res.append(' | '.join([''] + list(sub) + ['']).strip())
        res.append(h1)
    return '\n'.join(res)
