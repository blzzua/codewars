# https://www.codewars.com/kata/5919f3bf6589022915000023

def rotate_against_clockwise(matrix, times):
    if times % 4 == 0:
        return matrix
    rotated = [list(line) for line in zip(*matrix)][::-1]
    if times % 4 == 1:
        return rotated
    return rotate_against_clockwise(rotated, times - 1)


# clever numpy:
np.rot90(matrix, times).tolist()

