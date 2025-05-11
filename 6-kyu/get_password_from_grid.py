# https://www.codewars.com/kata/58f6e7e455d7597dcc000045

def find_x(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'x':
                return (i,j)
            
def get_password(grid, directions):
    i,j = find_x(grid)
    max_i, max_j = len(grid), len(grid[0])
    res = []
    for d in directions:
        if 'right' in d:
            j = (j + 1) %  max_j
        elif 'left' in d:
            j = (j - 1 + max_j) %  max_j
        elif 'down' in d:
            i = (i + 1) %  max_i
        elif 'up' in d:
            i = (i - 1 + max_i) %  max_i
        if d[-1] == 'T':
            res.append(grid[i][j])
    return ''.join(res)

