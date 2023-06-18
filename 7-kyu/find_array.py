# https://www.codewars.com/kata/59a2a3ba5eb5d4e609000055

def find_array(arr1, arr2):
    return [*map(arr1.__getitem__, filter(lambda x: x<len(arr1),arr2))]
