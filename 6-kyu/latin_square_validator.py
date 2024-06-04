# https://www.codewars.com/kata/646254375cee7a000ffaa404

def verify_latin_square(array, m):
    if len(set([len(line) for line in array])) > 1:
        return 'Array not square'
    if len(set([len(line) for line in zip(*array)])) > 1:
        return 'Array not square'
    if len(array) != m or len(array[0]) != m:
        return 'Array is wrong size'

    for i in range(m):
        seen_in_col = []
        seen_in_row = []
        for j in range(m):

            if not(0< array[i][j] <= m):
                return f'{array[i][j]} at {i+1},{j+1} is not between 1 and {m}'
            
            if array[i][j] in seen_in_row:
                return f'{array[i][j]} occurs more than once in row {i+1}'
            else:
                seen_in_row.append(array[i][j])

            if array[j][i] in seen_in_col:
                return f'{array[j][i]} occurs more than once in column {i+1}'
            else:
                seen_in_col.append(array[j][i])
            
    return f'Valid latin square of size {m}'
    
