# https://www.codewars.com/kata/59a1ea8b70e25ef8e3002992

def describe_the_shape(n):
    if n < 3: 
        return 'this will be a line segment or a dot'
    else:
        return f'This shape has {n} sides and each angle measures {180*(n-2)//n}'

