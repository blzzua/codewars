# https://www.codewars.com/kata/55af0d33f9b829d0a800008d

from itertools import cycle
def get_diagonale_code(grid: str) -> str:
    res = []
    a = [line.split(' ') for line in grid.split('\n')]
    n = len(a)
    if n < 2:
        return grid
    igen = cycle(list(range(n-1)) + list(range(n-1, -0, -1)))
    j, up =  0, False
    while True:
        i = next(igen)
        try:
            res.append(a[i][j])
        except IndexError:
            return ''.join(res)
        j += 1
