# https://www.codewars.com/kata/582f52208278c6be55000067

def round_to_five(numbers):
    return [5*(i//5) if abs(i - 5*(i//5)) < abs(i - 5*((i//5)+1)) else 5*((i//5)+1) for i in numbers ]


