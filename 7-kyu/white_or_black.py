# https://www.codewars.com/kata/563319974612f4fa3f0000e0

def square_color(file, rank):
    return ['white', 'black'][('abcdefgh'.index(file) + rank) % 2]
