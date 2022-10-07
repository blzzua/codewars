# https://www.codewars.com/kata/5a4138acf28b82aa43000117

def adjacent_element_product(array):
    return max(a*b for a,b in zip(array,array[1:]))

