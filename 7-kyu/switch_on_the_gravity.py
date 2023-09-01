# https://www.codewars.com/kata/64c743cb0a2a00002856ff73

def switch_gravity(lst):
    line = lst[0]
    sharps = []
    for i, val in enumerate(line):
        sharps.append(sum(1 for line in lst if line[i] == '#'))

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if len(lst) - i > sharps[j]:
                lst[i][j] = '-'
            else:
                lst[i][j] = '#'
    return lst
