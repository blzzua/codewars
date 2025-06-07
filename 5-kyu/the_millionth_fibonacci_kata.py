# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26

def mmul(A, B):
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]
    
def mpow(matrix, p):
    res =  [[1, 0], [0, 1]]
    base = matrix

    while p > 0:
        if p % 2 == 1:
            res = mmul(res, base)
        base = mmul(base, base)
        p = p//2

    return res

def fib(n):
    sign = 1 if (n > 0 or abs(n) % 2 == 1) else -1
    n = abs(n)
    if n == 0:
        return 0
    elif n == 1:
        return sign * 1
    res = mpow([[1, 1], [1, 0]], n-1)
    return sign*res[0][0]
