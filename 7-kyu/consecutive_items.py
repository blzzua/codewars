# https://www.codewars.com/kata/5f6d533e1475f30001e47514

def consecutive(arr, a, b):
    if abs(arr.index(a) - arr.index(b)) == 1:
        return True
    else:
        return False

