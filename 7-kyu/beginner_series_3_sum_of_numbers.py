# https://www.codewars.com/kata/55f2b110f61eb01779000053

def get_sum(*ab):
    a,b = sorted(ab)
    if a == b:
        return a
    return sum(i for i in range(a, b+1))


