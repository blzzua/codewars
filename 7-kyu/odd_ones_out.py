# https://www.codewars.com/kata/5d376cdc9bcee7001fcb84c0

def odd_ones_out(numbers):
    return [i for i in numbers if numbers.count(i) % 2 == 0]

