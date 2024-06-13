# https://www.codewars.com/kata/557e8a141ca1f4caa70000a6

def is_triangle_number(number):
    print(number)
    if not isinstance(number, int):
        return False
    if number < 0:
        return False
        
    res = int( 1/2 * (((8*number + 1)**0.5) - 1))
    return  res*(res+1) // 2 == number

