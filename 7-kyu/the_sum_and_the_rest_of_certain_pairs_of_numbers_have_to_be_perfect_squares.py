# https://www.codewars.com/kata/561e1e2e6b2e78407d000011

def is_square(n):
    if n > 0 and int(n ** 0.5)**2 == n :
        return True
    else:
        return False

# var1. precalculated 
MAX_NUM = 3000
from itertools import product

precalc = [(i,j) for i,j in product([*range(1,MAX_NUM)],[*range(1,MAX_NUM)]) if is_square(i+j) and is_square(i-j)][::-1]

# var2. little optimization
precalc = []
for i in range(MAX_NUM):
    for j in range(i,0,-1):
        if is_square(i+j) and is_square(i-j):
            precalc.append((i,j))
            break
precalc = precalc[::-1]

# solution:
def closest_pair_tonum(upper_lim):
    return next(filter(lambda x: x[0] < upper_lim, precalc))




#######  without bruteforce:
from itertools import combinations

def is_square(n):
    if n > 0 and int(n ** 0.5)**2 == n :
        return True
    else:
        return False
    
def closest_pair_tonum(upper_lim):
    for i, j in combinations(range(upper_lim - 1, 0, -1), 2):
        if is_square(i+j) and is_square(i-j):
            return (i,j)
