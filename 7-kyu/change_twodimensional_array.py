# https://www.codewars.com/kata/581214d54624a8232100005f

def matrix(array): 
    for i in range(len(array)):
        array[i][i] = 0 if array[i][i] < 0 else 1
    return array

