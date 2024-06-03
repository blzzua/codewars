# https://www.codewars.com/kata/5791bdba3467db61ff000040

# naive solution works but not pass Execution Timed Out (12000 ms)
def calc(matrix, n):
    matrix_size=len(matrix)
    acum = [line[:] for line in matrix]
    for power in range(n-1):
        res = [[0]*matrix_size for line in matrix]
        for row in range(matrix_size): 
            for col in range(matrix_size):
                for element in range(matrix_size):
                    res[row][col] += acum[row][element] * matrix[element][col]
        acum = [line[:] for line in res]
    return res


# solution works but not pass Execution Timed Out (12000 ms)
# the way of optimization: if n is large, then factor it, find the factors and remember the successive raising to the power, raise the squares of the matrices, etc.

def multiply_two_square_matrices(A, B):
	return [[sum([a*b for a,b in zip(row, col)]) for col in list(zip(*B))] for row in A]

def calc(matrix, n):
	if n % 2 == 1: 
        return multiply(matrix, calc(multiply_two_square_matrices(matrix, matrix), (n - 1) // 2))
	else: # n % 2 == 0
        return calc(multiply_two_square_matrices(matrix, matrix), n // 2)
