# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3

def clean_string(s):
    res = []
    for c in s:
        if c == '#':
            if res:
                res.pop()
        else:
            res.append(c)
    return ''.join(res)
