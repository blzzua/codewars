# https://www.codewars.com/kata/59f061773e532d0c87000d16

def elevator_distance(array):
     return sum(abs(a-b) for a, b in zip(array, array[1:]))

