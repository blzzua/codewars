# https://www.codewars.com/kata/593e978a3bb47a8308000b8f

from copy import deepcopy
def rotate_clockwise(matrix):
    res = []
    for line in zip(*reversed(matrix)):
        res.append(''.join(line))
    return res


# actual algorithm
if not len(matrix): return []
res = []
for x in range(len(matrix[0])):
    temp = []
    for y in range(len(matrix)-1,-1,-1):
        temp.append(matrix[y][x])
    res.append(''.join(temp))
return res
