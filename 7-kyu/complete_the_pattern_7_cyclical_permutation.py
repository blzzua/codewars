# https://www.codewars.com/kata/557592fcdfc2220bed000042

def pattern(n):
    s = [str(i)for i in range(1,n+1)]
    return '\n'.join( ''.join((s[i:]+s)[:n]) for i in range(n) )

