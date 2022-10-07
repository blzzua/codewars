# https://www.codewars.com/kata/544a54fd18b8e06d240005c0

def find_smallest(numbers,to_return):
    if to_return == 'value':
        return min(numbers)
    else:
        return numbers.index(min(numbers))

