# https://www.codewars.com/kata/558ac25e552b51dbc60000c3

def pattern(n):
    res = []
    for j in [*range(1,n)] + [*range(n,0,-1)]:
        i = j - 1 
        line = [' '] * ( 2 * n - 1)
        char = str((i+1) % 10)
        line[i], line[-i-1] = char, char
        res.append(''.join(line))
    return '\n'.join(res)
