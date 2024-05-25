# https://www.codewars.com/kata/573992c724fc289553000e95

def smallest(n):
    s = str(n)
    min_value, min_index1, min_index2 = n, 0, 0
    for j in range(len(s)):
        for i in range(len(s)):
            l = list(s)
            l.insert(i, l.pop(j))
            value = int(''.join(map(str,l)))
            if min_value > value:
                min_value = value
                min_index1 = j 
                min_index2 = i
    return [min_value, min_index1, min_index2]

# clever iteration over permutations:
# from itertools import permutations
# for i, j in permutations(range(len(str(n))), 2):
