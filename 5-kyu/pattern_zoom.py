# https://www.codewars.com/kata/56e6705b715e72fef0000647

def zoom(n):
    return '\n'.join(''.join('■□'[c] for c in line) for line in [[max(abs(n//2-x), abs(n//2-y)) % 2 for (x,y) in line ] for line in [[(x,y) for x in range(n)] for y in range(n)]])
