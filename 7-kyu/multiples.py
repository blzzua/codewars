# https://www.codewars.com/kata/55a8a36703fe4c45ed00005b

def multiple(x):
    print(x)
    res = ('Bang' if x % 3 == 0 else '') + ('Boom' if x % 5 == 0 else '')
    return res or 'Miss'
    

