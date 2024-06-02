# https://www.codewars.com/kata/5893eb36779ce5faab0000da

def matrix_elements_sum(matrix):
    haunted = set()
    res = 0
    for line in matrix:
        for i, room in enumerate(line):
            if i in haunted:
                continue
            if room == 0:
                haunted.add(i)
            else:
                res += room
    return res
