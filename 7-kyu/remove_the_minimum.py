# https://www.codewars.com/kata/563cf89eb4747c5fb100001b

def remove_smallest(numbers):
    n = numbers[:]
    if numbers:
        n.remove(min(numbers))
    return n


