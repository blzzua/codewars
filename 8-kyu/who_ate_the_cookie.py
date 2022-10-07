# https://www.codewars.com/kata/55a996e0e8520afab9000055

def cookie(x):
    if isinstance(x, str):
        res = 'Zach'
    elif type(x) in (float, int):
        res = 'Monica'
    else:
        res = 'the dog'
    return f'Who ate the last cookie? It was {res}!'

