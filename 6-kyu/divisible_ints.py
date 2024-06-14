# https://www.codewars.com/kata/566859a83557837d9700001a

def get_count(n):
    res = 0
    s = str(n)
    for i in range(len(s)):
        for j in range(i, len(s)):
            part = int(s[i:j+1])
            if part == n:
                continue
            if part != 0 and n % part == 0:
                res += 1
    return res
