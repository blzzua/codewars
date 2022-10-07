# https://www.codewars.com/kata/580dda86c40fa6c45f00028a

def cube_odd(arr):
    if all(type(i) == int for i in arr):
        return sum(i**3 for i in arr if i % 2 == 1)


