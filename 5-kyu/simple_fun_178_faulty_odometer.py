# https://www.codewars.com/kata/58b8d22560873d9068000085

def faulty_odometer(n):
    return int(str(n).translate(str.maketrans('56789','45678')), base=9)
