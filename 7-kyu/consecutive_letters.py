# https://www.codewars.com/kata/5ce6728c939bf80029988b57

from string import ascii_letters
def solve(st):
    print(st)
    return ''.join(sorted(st)) in ascii_letters

