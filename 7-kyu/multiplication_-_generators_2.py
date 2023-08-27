# https://www.codewars.com/kata/5637ead70013386e30000027

def generator(a):
    i = 0
    while True:
        i += 1
        yield f'{a} x {i} = {a*i}'
