# https://www.codewars.com/kata/64be6f070381860017dba5ab

def hex_distance(grid):
    xx = [(i, line.index('x')) for i,line in enumerate(grid) if 'x' in line]
    if len(xx) == 1: ## all x in single row
        dy = 0
        line = grid[xx[0][0]]
        first_x = xx[0][1]
        dx = line.find('x', first_x+1) - first_x
    else:
        dy, dx = [abs(x-y) for y, x  in zip(*xx)]
    res = dy + max(0, (dx-dy) // 2)
    return res
  
