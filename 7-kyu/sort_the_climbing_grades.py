# https://www.codewars.com/kata/58a08e622e7fb654a300000e

grades = {val:n for n, val in enumerate(['VB', 'V0', 'V0+'] + [f'V{i}' for i in range(1, -~17)])}

def sort_grades(lst):
    return sorted(lst, key=grades.get)

