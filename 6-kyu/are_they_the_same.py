# https://www.codewars.com/kata/550498447451fbbd7600041c

def comp(array1, array2):
    if not(array1 == None or array2 == None):
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    return False
