# https://www.codewars.com/kata/577c349edf78c178a1000108

def xmastree(n):
    return [''.join('_'*(n-i) + '#'*(2*i-1)+ '_'*(n-i)) for i in range(1,-~n)] \
    + [''.join('_'*(n-1) + '#'+ '_'*(n-1)),''.join('_'*(n-1) + '#'+ '_'*(n-1))]


