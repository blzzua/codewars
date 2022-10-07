# https://www.codewars.com/kata/5434283682b0fdb0420000e6

def caffeine_buzz(n):
    if n % 12 == 0:
        return 'CoffeeScript'
    elif n % 6 == 0:
        return 'JavaScript'
    elif n % 3 == 0:
        return 'Java'
    else:
        return 'mocha_missing!'

