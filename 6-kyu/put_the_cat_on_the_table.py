# https://www.codewars.com/kata/560030c3ab9f805455000098/solutions

def find_table(room):
    for i, line in enumerate(room):
        for j, char in enumerate(line):
            if char == 1:
                return [i,j]
    return None

def put_the_cat_on_the_table(cat, room):
    table = find_table(room)
    if not(0 <= cat[0] < len(room) and 0 <= cat[1] < len(room[0])):
        return 'NoCat'
    if table is None:
        return 'NoTable'
    UD = table[0] - cat[0]
    LR = table[1] - cat[1]
    res = ''
    if UD > 0:
        res = 'D' * UD 
    if UD < 0:
        res = 'U' * (-1 * UD )
    if LR > 0:
        res = res + 'R' * LR
    if LR < 0:
        res = res + 'L' * (-1 * LR)
    return res
