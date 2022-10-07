# https://www.codewars.com/kata/5ce969ab07d4b7002dcaa7a1

def solve(st):
    return max([i for i in range(1,len(st)//2+1) if st[0:i] == st[-i:]], default=0)


