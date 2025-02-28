# https://www.codewars.com/kata/58958ef541c9794213000090

def rows_rearranging(matrix):
    sorted_matrix = sorted(matrix)
    for row1, row2 in zip(sorted_matrix,sorted_matrix[1:]):
        if any([val1 >= val2 for val1, val2 in zip(row1, row2)]):
            return False
    return True
  
