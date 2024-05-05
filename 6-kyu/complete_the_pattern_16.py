# https://www.codewars.com/kata/55ae997d1c40a199e6000018

def pattern(n):
    s = [str(( n % 10 ))] * n
    res = []
    for i in range(n):
        for j in range(i,n):
            s[j] = str((n - i) % 10)
        res.append(''.join(s))
    return '\n'.join(res)
    
