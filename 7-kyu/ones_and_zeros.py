# https://www.codewars.com/kata/578553c3a1b8d5c40300037c

def binary_array_to_number(arr):
    return sum(2**i * b for i,b in enumerate(arr[::-1]))

