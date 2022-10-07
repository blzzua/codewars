# https://www.codewars.com/kata/56a4872cbb65f3a610000026

def max_rot(n):
    s=str(n)
    ret=[n]
    for i in range(len(s)):
        s=s[:i]+s[i+1:]+s[i]
        ret.append(int(s))
    return max(ret)

