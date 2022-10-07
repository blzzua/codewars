# https://www.codewars.com/kata/5b45e4b3f41dd36bf9000090

def sequence(x):
    return sorted(range(1,-~x), key=lambda i: str(i))

