# https://www.codewars.com/kata/54c27a33fb7da0db0100040e

def is_square(n):
    try:
        return (n**0.5).is_integer()
    except:
        return False

