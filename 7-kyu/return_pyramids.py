# https://www.codewars.com/kata/5a1c28f9c9fc0ef2e900013b

def pyramid(n):
    return '\n'.join(' '*(n-i)+'/'+ ('_' if n==i else ' ')*(i-1)*2 +'\\' for i in range(1,n+1)) + '\n'

