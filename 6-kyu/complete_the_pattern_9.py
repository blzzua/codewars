# https://www.codewars.com/kata/5579e6a5256bac65e4000060

def wavegen(n,m):
    # copied from another my solution from similar task
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

def pattern(n):
    res = []
    for i in [*range(1, n+1)] + [*range(1, n)][::-1]: # code reuse from https://www.codewars.com/kata/5575ff8c4d9c98bc96000042
        line = ' ' * (n-i) + ''.join(map(lambda x: x[-1],map(str,wavegen(i,1)))) + ' ' * (n-i )
        res.append(''.join(line))
    return '\n'.join(res)
