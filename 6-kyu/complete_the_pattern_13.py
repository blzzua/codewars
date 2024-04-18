# https://www.codewars.com/kata/5592e5d3ede9542ff0000057

def wavegen(n,m):
    i, grow = 0, 1
    while m > 0:
        if grow:
            if i < n:
                i += 1
            else:
                grow = 1 - grow
                continue
        else:
            if i >= 2:
                i -= 1
            else:
                grow= 1 - grow
                m -= 1
                continue
        yield i

def pattern(n, y=1, *args):
    res = []
    y = max(y,1)
    for j in wavegen(n,y):
        i = j - 1 
        line = [' '] * ( 2 * n - 1)
        char = str((i+1) % 10)
        line[i], line[-i-1] = char, char
        res.append(''.join(line))
    return '\n'.join(''.join(col) for col in zip(*res))
