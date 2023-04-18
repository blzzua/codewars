# https://www.codewars.com/kata/5a66ea69e6be38219f000110

def solve(s):
    ln_odd = len(s) % 2
    if s == s[::-1]:
        return bool(ln_odd)
    else:
        half = len(s)//2 
        w1 = s[:half]
        w2 = s[-half:][::-1]
        sum_diff = sum(a != b for a,b in zip(w1, w2))
        if ln_odd:
            return sum_diff < 2
        else:
            return sum_diff == 1
