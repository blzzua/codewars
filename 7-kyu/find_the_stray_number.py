# https://www.codewars.com/kata/57f609022f4d534f05000024

from random import choice
def stray(arr):
    return sum(arr) - choice(arr)*(len(arr)-1)  # i'm lucky

