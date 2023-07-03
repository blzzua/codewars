# https://www.codewars.com/kata/56143efa9d32b3aa65000016

def area(d):
    return (3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679 * d ** 2) / 4

def sum_circles(*args):
    return f'We have this much circle: {round(sum(map(area,args)))}'
