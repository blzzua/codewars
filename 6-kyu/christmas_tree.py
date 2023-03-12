# https://www.codewars.com/kata/52755006cc238fcae70000ed

def christmas_tree(n):
    return  '\n'.join([' ' * ( n - i ) + '*' * (2 * i - 1) + ' ' * ( n - i ) for i in range(1,n+1)])
