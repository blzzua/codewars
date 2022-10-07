# https://www.codewars.com/kata/593b1909e68ff627c9000186

def nickname_generator(name):
    if len(name) <= 3:
        return 'Error: Name too short'
    elif name[2].lower() in 'aeiou':
        return name[:4]
    else:
        return name[:3]

