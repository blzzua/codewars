# https://www.codewars.com/kata/56fcfad9c7e1fa2472000034

def evil(n):
    if bin(n)[2:].count('1') % 2:
        return  "It's Odious!"
    else:
        return "It's Evil!"

