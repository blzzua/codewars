# https://www.codewars.com/kata/590f5b4a7bbb3e246000007d

def comes_after(st, l): 
    return ''.join([l2 for l1, l2 in zip(st,st[1:]) if l1.lower() == l.lower() and l2.isalpha()])

