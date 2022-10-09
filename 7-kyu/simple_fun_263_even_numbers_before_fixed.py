# https://www.codewars.com/kata/5912701a89fc3d0a6a000169

def even_numbers_before_fixed(sequence, fixed_element):
    res = 0
    for i in sequence:
        if i == fixed_element:
            return res
        elif i % 2 == 0:
            res += 1
    else:
        return -1
