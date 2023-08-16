# https://www.codewars.com/kata/64cf34314e8a905162e32ff5

def smallest_transform(num):
    n = str(num)
    min_steps = 99999
    for td in set(n):
        steps = sum(abs(int(d) - int(td)) for d in n)
        print()
        if min_steps > steps:
            min_steps = steps
    return min_steps
