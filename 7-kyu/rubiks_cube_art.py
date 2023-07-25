# https://www.codewars.com/kata/6387ea2cf418c41d277f3ffa

def cube(n):
    uf =  '/\\'
    ub =  '_\\'
    df =  '\\/'
    db =  '_/'
    res = []
    for i in range(1, n+1):
        res.append(' ' * (n-i) + uf * i + ub * n)
    for i in range(n, 0, -1 ):
        res.append( ' ' * (n-i) + df * i + db * n)
    return '\n'.join(res)
