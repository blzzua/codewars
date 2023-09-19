# https://www.codewars.com/kata/5bbad1082ce5333f8b000006

def stack_height_3d(layers):
    if layers <= 1:
        return layers
    else:
        return (layers - 1) * (( 2 / 3) ** 0.5 ) + 1
