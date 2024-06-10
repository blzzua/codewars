# https://www.codewars.com/kata/62c376ce1019024820580309

from string import ascii_uppercase as al
def get_cell_addresses(cell_range):
    res = []
    start, end = [ (cell[0], int(cell[1:])) for cell in cell_range.split(':')]
    if start == end:
        return res
    letter_start_index = al.index(start[0])
    letter_end_index = al.index(end[0])
    for num in range(start[1], end[1]+1):
        for letter in range(letter_start_index, letter_end_index+1):
            res.append(f'{al[letter]}{num}')
    return res
