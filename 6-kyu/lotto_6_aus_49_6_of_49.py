# https://www.codewars.com/kata/57a98e8172292d977b000079

from numpy import random
def number_generator():
    res = sorted(random.choice(range(1,50), size=6, replace=False)) + [random.randint(0,10)]
    return res

def check_for_winning_category(your_numbers, winning_numbers):
    my_numbers, my_winning_numbers = your_numbers[:], winning_numbers[:]
    superzahl = (my_winning_numbers.pop() ==  my_numbers.pop())
    numbers = sum(bool(i in my_winning_numbers) for i in my_numbers)
    match numbers, superzahl:
        case 6, True : return 1
        case 6, False: return 2
        case 5, True : return 3
        case 5, False: return 4
        case 4, True : return 5
        case 4, False: return 6
        case 3, True : return 7
        case 3, False: return 8
        case 2, True : return 9
        case _: return -1
