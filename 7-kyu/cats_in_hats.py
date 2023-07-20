# https://www.codewars.com/kata/57b5907920b104772c00002a

def height(n):
    return '{0:.3f}'.format( 2000000 * sum((4 ** i ) / (10 ** i )  for i in range(n+1)))
