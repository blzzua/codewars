# https://www.codewars.com/kata/558d5c71c68d1e86b000010f

from itertools import product as P
from collections import Counter
# precompute
vampires = []    

for L in (2,3):
    G = [range(0,10) for _ in range(L)]
    limit1 = 10**(2*L-1)
    limit2 = 10**L**2-1
    for a,b in P(P(*G), P(*G)): 
        p = int(''.join(map(str,a))) * int(''.join(map(str,b)))
        if limit1 < p < limit2 and Counter(str(p)) == Counter(map(str,a+b)) and a[-1]+b[-1] != 0: 
            vampires.append(p)
vampires = sorted(list(set(vampires)))

def vampire_number(k):
    return vampires[k-1]


# clever
is_vampire = lambda x, y: sorted(f"{x}{y}") == sorted(f"{x*y}") and x%10 + y%10 > 0
vampires = sorted({x*y for p in (1, 2) for x in range(10**p, 10**(p+1)) for y in range(x, 10**(p+1)) if is_vampire(x, y)})

# ya clever
vampires = set()
for i in [1, 2]:
    for x, y in combinations(range(10**i, 10**(i+1)), 2):
        if x % 10 == 0 == y % 10:
            continue
        z = x * y
        if sorted(str(z)) == sorted(f'{x}{y}'):
            vampires.add(z)
xs = sorted(vampires)

