# https://www.codewars.com/kata/5a7b3d08fd5777bf6a000121

def remove_nth_element(lst, n):
    # Fix it
    lst_copy = lst[:]
    del lst_copy[n]
    return lst_copy

