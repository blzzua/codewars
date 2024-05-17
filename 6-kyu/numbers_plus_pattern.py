# https://www.codewars.com/kata/563cb92e0996a4ac0b000042

def pattern(n):
    res = []
    for i in list(range(1,n)) + list(range(n,0,-1)):
        if i == n:
            res.append(''.join(str(i%10)for i in list(range(1,n)) + list(range(n,0,-1))))
        else:
            res.append(' '*(n - 1) + str(i%10))
    return '\n'.join(res)+'\n'
