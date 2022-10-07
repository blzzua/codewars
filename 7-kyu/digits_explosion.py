# https://www.codewars.com/kata/585b1fafe08bae9988000314

def explode(s):
    return ''.join([i * int(i) for i in s])


