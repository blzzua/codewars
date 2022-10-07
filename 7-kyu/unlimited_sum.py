# https://www.codewars.com/kata/536c738e49aa8b663b000301

origsum = sum
def sum(*args):
    return origsum([i for i in args if type(i) == int])

