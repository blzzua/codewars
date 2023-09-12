# https://www.codewars.com/kata/5bb804397274c772b40000ca

def stack_height_2d(layers):
    if layers:
        return (((layers - 1) ** 2) - (((layers - 1) / 2) ** 2)) ** 0.5 + 1
    else:
        return 0
