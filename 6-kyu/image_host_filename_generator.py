# https://www.codewars.com/kata/586a933fc66d187b6e00031a

from string import ascii_uppercase
from itertools import product
def generateName():
    # really ugly solution. better use the random.choice/uuid or enclosure.
    for letters in product(*[ascii_uppercase] * 6):
        candidate = ''.join(letters)
        if not photoManager.nameExists(candidate):
            return candidate


# enclosing
from string import ascii_uppercase
from itertools import product

def name_generator_function():
    for letters in product(*[ascii_uppercase] * 6):
        candidate = ''.join(letters)
        if not photoManager.nameExists(candidate):
            yield candidate

name_generator = name_generator_function()
def generateName():
    return next(name_generator)
