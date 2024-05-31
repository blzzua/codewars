# https://www.codewars.com/kata/5782dd86202c0e43410001f6

from itertools import cycle
from functools import reduce
from operator import add, sub, mul, truediv

def do_math(st) :
    intermediate = []
    for chunk in st.split():
        numbers = []
        for ch in chunk:
            if ch.isdigit():
                numbers.append(ch)
            else:
                letter = ch
        intermediate.append((letter, int(''.join(numbers))))
    numbers = [number for letter, number in sorted(intermediate, key=lambda x: (x[0], -x[1]))]   # unstable, probability sort order 
    ops = cycle([add, sub, mul, truediv])
    return round(reduce( lambda a,b: next(ops)(a,b), numbers))


# regex parsing phase:
for ch in s.split():
    a, b, c = re.compile(r"(\d*)([a-z])(\d*)").fullmatch(ch).groups()
    intermediate.append(b, int(a + c))
