# https://www.codewars.com/kata/5805f0663f1f9c49be00011f

def present(x,y):
    if x == 'goodpresent':
        return ''.join(chr(ord(c) + y) for c in x)
    elif x == 'crap' or x == 'empty':
        return ''.join(sorted(x))
    elif x == 'bang':
        return str(sum([ord(i)-y for i in x]))
    elif x == 'dog':
        return f'pass out from excitement {y} times'
    elif x == 'badpresent':
        return 'Take this back!'
    else:
        return None
    

